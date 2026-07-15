#!/usr/bin/env python3
"""Generate transparent ATS-readiness reports for resume artifact sets."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

VERSION = "0.2.1"
STANDARD_HEADINGS = {
    "summary",
    "technical skills",
    "skills",
    "professional experience",
    "experience",
    "education",
}
CONTACT_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "phone": re.compile(r"(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}"),
}
DATE_PATTERN = re.compile(
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)\s+\d{4}\b|\b\d{4}\s*[-–]\s*(?:\d{4}|Present)\b",
    re.I,
)
BAD_GLYPHS = ("�", "□", "■", "\x00")
STOPWORDS = {
    "the", "and", "or", "to", "of", "a", "in", "for", "with", "on", "as",
    "is", "are", "be", "will", "you", "we", "our", "this", "that", "from",
    "at", "by", "an", "have", "has", "using", "work", "role", "team",
    "experience", "years", "including", "across", "their", "they", "your",
}
ALIASES = {
    "c/c++": {"c", "c++", "c/c++"},
    "tcp": {"tcp", "tcp/ip"},
    "open source": {"open source", "open-source", "github", "public repositories"},
    "nri": {"nri", "node resource interface"},
    "kubelet": {"kubelet", "kubelets"},
    "ai/ml": {"ai/ml", "machine learning", "ml workloads"},
}
LIMITING_PHRASES = (
    "experimental",
    "experiments",
    "exploratory",
    "familiarity",
    "familiar with",
    "fundamentals",
    "conceptual",
    "has not",
    "have not",
    "without claiming",
    "not production",
)


@dataclass
class CategoryScore:
    score: int
    findings: list[str]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"[`*_>#|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokens(text: str) -> list[str]:
    values = re.findall(r"[A-Za-z][A-Za-z0-9+#./-]*", text.lower())
    return [value for value in values if value not in STOPWORDS and len(value) > 1]


def extract_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_docx(path: Path) -> str:
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", namespace):
        parts = [node.text or "" for node in paragraph.findall(".//w:t", namespace)]
        if parts:
            paragraphs.append("".join(parts))
    return "\n".join(paragraphs)


def extract_pdf(path: Path) -> str:
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "pdf.txt"
        process = subprocess.run(
            ["pdftotext", "-layout", str(path), str(output)],
            text=True,
            capture_output=True,
            check=False,
        )
        if process.returncode != 0:
            raise RuntimeError(process.stderr.strip() or "pdftotext failed")
        return output.read_text(encoding="utf-8", errors="replace")


def headings(markdown: str) -> list[str]:
    return [
        re.sub(r"^#+\s*", "", line).strip().lower()
        for line in markdown.splitlines()
        if re.match(r"^#{1,3}\s+", line)
    ]


def coverage(source: str, artifact: str) -> float:
    source_tokens = set(tokens(normalize(source)))
    artifact_tokens = set(tokens(normalize(artifact)))
    return 1.0 if not source_tokens else len(source_tokens & artifact_tokens) / len(source_tokens)


def score_parseability(markdown: str, docx: str, pdf: str) -> CategoryScore:
    findings: list[str] = []
    docx_coverage = coverage(markdown, docx)
    pdf_coverage = coverage(markdown, pdf)
    score = 100
    for name, value in (("DOCX", docx_coverage), ("PDF", pdf_coverage)):
        if value < 0.80:
            score -= 35
        elif value < 0.90:
            score -= 20
        elif value < 0.96:
            score -= 8
        findings.append(f"{name} token coverage versus Markdown: {value:.1%}.")
    for name, text in (("DOCX", docx), ("PDF", pdf)):
        bad = [glyph for glyph in BAD_GLYPHS if glyph in text]
        if bad:
            score -= 15
            findings.append(
                f"{name} contains suspicious or corrupted glyphs: "
                + ", ".join(repr(glyph) for glyph in bad)
                + "."
            )
    if len(normalize(pdf)) < 500:
        score -= 40
        findings.append("PDF extraction returned unusually little text.")
    return CategoryScore(max(0, score), findings)


def score_completeness(markdown: str) -> CategoryScore:
    findings: list[str] = []
    score = 100
    document_headings = set(headings(markdown))
    for label, pattern in CONTACT_PATTERNS.items():
        if not pattern.search(markdown):
            score -= 15
            findings.append(f"Missing recognizable {label}.")
    for heading in ("summary", "professional experience", "education"):
        if not any(heading == value or heading in value for value in document_headings):
            score -= 15
            findings.append(f"Missing conventional {heading.title()} heading.")
    if len(DATE_PATTERN.findall(markdown)) < 3:
        score -= 15
        findings.append("Work-history dates may be incomplete or inconsistently parseable.")
    if re.search(r"\b(TODO|TBD|PLACEHOLDER|FIXME)\b", markdown, re.I):
        score -= 30
        findings.append("Placeholder text remains.")
    if not findings:
        findings.append("Contact details, conventional sections, and work-history dates are present.")
    return CategoryScore(max(0, score), findings)


def extract_requirements(job: str) -> tuple[list[str], list[str]]:
    required: list[str] = []
    preferred: list[str] = []
    mode: str | None = None
    for raw in job.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            heading = re.sub(r"^#+\s*", "", stripped).strip().lower().rstrip(":")
            if heading in {
                "what we are looking for",
                "what we're looking for",
                "what we’re looking for",
                "required qualifications",
                "requirements",
                "qualifications",
                "what you will bring",
            }:
                mode = "required"
            elif heading in {
                "additionally helpful experience",
                "preferred qualifications",
                "preferred experience",
                "nice to have",
                "bonus qualifications",
            }:
                mode = "preferred"
            else:
                # Metadata, responsibilities, compensation, and narrative context
                # are deliberately excluded from qualification scoring.
                mode = None
            continue
        if mode and stripped.startswith(("-", "*", "•")):
            line = stripped.lstrip("-*• ").strip()
            if len(line.split()) >= 3:
                (required if mode == "required" else preferred).append(line)
    return required[:25], preferred[:20]


def phrase_present(phrase: str, resume_lower: str) -> bool:
    options = ALIASES.get(phrase, {phrase})
    return any(
        re.search(rf"(?<![a-z0-9]){re.escape(option)}(?![a-z0-9])", resume_lower)
        for option in options
    )


def evidence_lines(terms: list[str], resume: str) -> list[str]:
    matches: list[str] = []
    for line in resume.lower().splitlines():
        if any(phrase_present(term, line) for term in terms):
            matches.append(line.strip())
    return matches


def requirement_match(requirement: str, resume: str) -> tuple[str, float, list[str]]:
    req_lower = requirement.lower()
    resume_lower = resume.lower()
    requirement_tokens = list(dict.fromkeys(tokens(requirement)))
    matched = [term for term in requirement_tokens if phrase_present(term, resume_lower)]
    ratio = len(matched) / max(1, len(requirement_tokens))
    contexts = evidence_lines(matched, resume)
    limiting = any(
        phrase in context for context in contexts for phrase in LIMITING_PHRASES
    )

    # These requirements need capability evidence, not mere keyword overlap.
    if "minimum of 5 years" in req_lower and "8+ years" in req_lower:
        direct = bool(re.search(r"(?:more than|over)\s+(?:8|[12]\d)\s+years", resume_lower)) and (
            "compute" in resume_lower and "infrastructure" in resume_lower
        )
        return ("direct" if direct else "adjacent" if ratio >= 0.25 else "missing",
                1.0 if direct else ratio, matched)
    if "proficiency in go, java, or c/c++" in req_lower:
        language_section = "\n".join(
            line for line in resume_lower.splitlines()
            if "languages:" in line or line.startswith("**languages")
        )
        direct = bool(re.search(r"(?<![a-z])go(?![a-z])", language_section)) or any(
            value in language_section for value in ("c++", "c/c++", " c,")
        )
        return ("direct" if direct else "missing", 1.0 if direct else 0.0,
                ["Go/C/C++"] if direct else [])
    if "contribute to the upstream" in req_lower:
        direct = bool(re.search(
            r"(contributed|contributions?)\s+to\s+(?:the\s+)?(?:upstream|kubernetes|containerd)",
            resume_lower,
        ))
        return ("direct" if direct else "missing", 1.0 if direct else ratio,
                ["upstream contributions"] if direct else matched)
    if "linux kernel development" in req_lower:
        direct = bool(re.search(
            r"linux kernel (?:module|modules|development|patch|patches|contribution|contributions)",
            resume_lower,
        )) and not any(phrase in resume_lower for phrase in ("has not written", "without claiming"))
        if direct:
            return "direct", ratio, matched
        if "linux kernel" in resume_lower and (
            "freebsd kernel" in resume_lower or "kernel-module development" in resume_lower
        ):
            return "adjacent", ratio, matched
        return "missing", ratio, matched
    if "ai/ml workloads" in req_lower:
        direct = bool(re.search(
            r"(?:managed|operated|supported|owned).{0,100}(?:ai/ml|machine learning|ml workloads)",
            resume_lower,
        ))
        return ("direct" if direct else "missing", 1.0 if direct else ratio,
                matched if direct else [])
    if "customizations and plugins" in req_lower:
        if re.search(r"(?:developed|maintained|built|implemented).{0,100}(?:containerd|kubernetes).{0,100}(?:customizations?|plugins?)", resume_lower):
            return "direct", ratio, matched
        if any(term in resume_lower for term in ("containerd", "nri plugin")):
            return "adjacent", ratio, matched
        return "missing", ratio, matched
    if "runtimes as a service" in req_lower:
        if re.search(r"(?:production|operated|supported).{0,100}(?:container runtime|containerd|runc|kubelet)", resume_lower) and not limiting:
            return "direct", ratio, matched
        if any(term in resume_lower for term in ("kubernetes", "kubelet", "containerd", "runc")):
            return "adjacent", ratio, matched
        return "missing", ratio, matched
    if "debugging system performance issues in a linux environment" in req_lower:
        direct = "linux" in resume_lower and bool(re.search(
            r"(?:debugged|debugging|diagnosed|troubleshooting).{0,100}(?:performance|runtime|system)",
            resume_lower,
        ))
        return ("direct" if direct else "adjacent" if ratio >= 0.25 else "missing",
                1.0 if direct else ratio, matched)
    if "designing large-scale distributed systems" in req_lower:
        direct = "large-scale distributed systems" in resume_lower or (
            "distributed systems" in resume_lower and "kubernetes" in resume_lower
        )
        return ("direct" if direct else "adjacent" if ratio >= 0.25 else "missing",
                1.0 if direct else ratio, matched)
    if "thrive in ambiguity" in req_lower:
        adjacent = "evolving requirements" in resume_lower and "competing priorities" in resume_lower
        return ("adjacent" if adjacent else "missing", 0.55 if adjacent else ratio,
                ["evolving requirements", "competing priorities"] if adjacent else matched)
    if "communication and collaboration skills" in req_lower:
        direct = "collaborated" in resume_lower and "engineering teams" in resume_lower
        return ("direct" if direct else "adjacent" if ratio >= 0.25 else "missing",
                1.0 if direct else ratio, matched)
    if "open source projects" in req_lower:
        direct = bool(re.search(r"(?:contributed|contributions?)\s+to.{0,80}open.source", resume_lower))
        if direct:
            return "direct", ratio, matched
        if "github.com/" in resume_lower or "public repositories" in resume_lower:
            return "adjacent", ratio, matched
        return "missing", ratio, matched

    strength = "direct" if ratio >= 0.55 else "adjacent" if ratio >= 0.25 else "missing"
    return strength, ratio, matched


def score_requirements(requirements: list[str], resume: str, label: str) -> CategoryScore:
    if not requirements:
        return CategoryScore(
            0,
            [f"No {label.lower()} requirements were available; targeted scoring is incomplete."],
        )
    points: list[int] = []
    findings: list[str] = []
    for requirement in requirements:
        strength, _, matched = requirement_match(requirement, resume)
        points.append(100 if strength == "direct" else 55 if strength == "adjacent" else 0)
        findings.append(
            f"{strength.title()}: {requirement} "
            f"(matched: {', '.join(matched[:8]) or 'none'})."
        )
    return CategoryScore(round(sum(points) / len(points)), findings)


def score_language(markdown: str, requirements: list[str]) -> CategoryScore:
    findings: list[str] = []
    score = 100
    resume_tokens = tokens(markdown)
    total = max(1, len(resume_tokens))
    if len(set(resume_tokens)) / total < 0.32:
        score -= 12
        findings.append("Vocabulary is highly repetitive.")
    if len(resume_tokens) > 1300:
        score -= 10
        findings.append("Resume is unusually dense for ATS and recruiter review.")
    action_hits = len(
        re.findall(
            r"(?m)^[-*]\s+(?:Architected|Built|Designed|Developed|Implemented|Led|"
            r"Created|Automated|Modernized|Rebuilt|Served)\b",
            markdown,
            re.I,
        )
    )
    if action_hits < 8:
        score -= 10
        findings.append("Relatively few bullets begin with strong action verbs.")
    if requirements:
        requirement_tokens = set(tokens(" ".join(requirements)))
        overlap = len(requirement_tokens & set(resume_tokens)) / max(1, len(requirement_tokens))
        findings.append(f"Qualification-language token coverage: {overlap:.1%}.")
        if overlap < 0.35:
            score -= 20
        elif overlap < 0.50:
            score -= 10
    if not findings:
        findings.append("Language is specific, action-oriented, and readable.")
    return CategoryScore(max(0, score), findings)


def score_human(markdown: str) -> CategoryScore:
    findings: list[str] = []
    score = 100
    lines = markdown.splitlines()
    first_third = "\n".join(lines[:35]).lower()
    if not any(
        phrase in first_third
        for phrase in (
            "distributed systems",
            "systems software",
            "infrastructure",
            "software architect",
            "backend",
        )
    ):
        score -= 15
        findings.append("Target positioning is not explicit in the first third.")
    bullets = [line for line in lines if line.startswith("- ")]
    metric_bullets = sum(bool(re.search(r"\d", bullet)) for bullet in bullets)
    if metric_bullets < 4:
        score -= 12
        findings.append("Few bullets include scale or measurable context.")
    long_bullets = sum(len(bullet) > 240 for bullet in bullets)
    if long_bullets:
        score -= min(15, long_bullets * 3)
        findings.append(f"{long_bullets} bullets are long enough to hinder scanning.")
    if not findings:
        findings.append("The first third is role-specific and evidence is easy to scan.")
    return CategoryScore(max(0, score), findings)


def disposition(score: int, critical: list[str], targeted_complete: bool) -> str:
    if critical or not targeted_complete:
        return "Not Ready"
    if score >= 90:
        return "Submission Ready"
    if score >= 80:
        return "Strong"
    if score >= 70:
        return "Needs Revision"
    return "Not Ready"


def render_report(
    args: argparse.Namespace,
    scores: dict[str, tuple[CategoryScore, int]],
    overall: int,
    final_disposition: str,
    critical: list[str],
    requirement_rows: list[tuple[str, str, str, list[str]]],
    hashes: dict[str, str],
    targeted_complete: bool,
) -> str:
    validated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    output = [
        "# ATS Readiness Report",
        "",
        f"- **Validated:** {validated}",
        f"- **Validator:** CareerPortfolio ATS Validator v{VERSION}",
        f"- **Score type:** {'Targeted readiness' if args.job else 'Generic baseline'}",
        f"- **Overall score:** {overall}/100",
        f"- **Disposition:** {final_disposition}",
        f"- **Autonomous revision pass:** {args.pass_number} of 3",
        "",
    ]
    if not targeted_complete and args.job:
        output.extend(
            [
                "> **Targeted score incomplete:** the supplied job description did not yield "
                "explicit required/preferred bullet requirements. Preserve this report, but do "
                "not treat the overall score as submission-ready.",
                "",
            ]
        )
    output.extend(
        [
            "## Category Scores",
            "",
            "| Category | Score | Weight |",
            "|---|---:|---:|",
        ]
    )
    for name, (category, weight) in scores.items():
        output.append(f"| {name} | {category.score} | {weight}% |")
    output.extend(["", "## Critical Failures", ""])
    output.extend([f"- {failure}" for failure in critical] or ["- None detected."])
    for name, (category, _) in scores.items():
        output.extend(["", f"## {name}", ""])
        output.extend(f"- {finding}" for finding in category.findings)
    if requirement_rows:
        output.extend(
            [
                "",
                "## Requirement-to-Evidence Matrix",
                "",
                "| Type | Strength | Requirement | Matched terms |",
                "|---|---|---|---|",
            ]
        )
        for requirement_type, strength, requirement, matched in requirement_rows:
            output.append(
                f"| {requirement_type} | {strength.title()} | "
                f"{requirement.replace('|', '/')} | {', '.join(matched[:10]) or 'None'} |"
            )
    output.extend(["", "## Artifact Versions", ""])
    output.extend(f"- `{name}`: `{value}`" for name, value in hashes.items())
    output.extend(["", "## Recommended Next Action", ""])
    if final_disposition == "Submission Ready":
        output.append("- Submit after final human visual review.")
    elif final_disposition == "Strong":
        output.append(
            "- Review the listed deductions and submit unless a safe, evidence-backed "
            "improvement is material."
        )
    elif not targeted_complete and args.job:
        output.append("- Capture the exact job posting in a repository file, then rerun targeted validation.")
    else:
        output.append(
            "- Revise the lowest-scoring fixable categories, regenerate artifacts, and rerun "
            "validation. Stop after three autonomous passes or earlier when a stop condition is reached."
        )
    return "\n".join(output) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", type=Path, required=True)
    parser.add_argument("--docx", type=Path, required=True)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--job", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--pass-number", type=int, default=0, choices=range(0, 4))
    args = parser.parse_args()

    for path in (args.resume, args.docx, args.pdf):
        if not path.exists():
            parser.error(f"missing input: {path}")

    markdown = extract_markdown(args.resume)
    docx = extract_docx(args.docx)
    pdf = extract_pdf(args.pdf)
    job = args.job.read_text(encoding="utf-8") if args.job else None

    parseability = score_parseability(markdown, docx, pdf)
    completeness = score_completeness(markdown)
    human = score_human(markdown)
    requirement_rows: list[tuple[str, str, str, list[str]]] = []

    if job:
        required, preferred = extract_requirements(job)
        required_score = score_requirements(required, markdown, "Required")
        preferred_score = (
            score_requirements(preferred, markdown, "Preferred")
            if preferred
            else CategoryScore(100, ["No explicit preferred requirements were listed."])
        )
        language = score_language(markdown, required + preferred)
        for requirement_type, requirements in (("Required", required), ("Preferred", preferred)):
            for requirement in requirements:
                strength, _, matched = requirement_match(requirement, markdown)
                requirement_rows.append((requirement_type, strength, requirement, matched))
        scores = {
            "Artifact parseability and structure": (parseability, 25),
            "Required-information completeness": (completeness, 10),
            "Required job-requirement evidence": (required_score, 30),
            "Preferred job-requirement evidence": (preferred_score, 15),
            "Language and keyword quality": (language, 10),
            "Human readability and positioning": (human, 10),
        }
        targeted_complete = bool(required)
    else:
        language = score_language(markdown, [])
        scores = {
            "Artifact parseability and structure": (parseability, 50),
            "Required-information completeness": (completeness, 20),
            "Language and keyword quality": (language, 15),
            "Human readability and positioning": (human, 15),
        }
        targeted_complete = True

    overall = round(
        sum(category.score * weight for category, weight in scores.values())
        / sum(weight for _, weight in scores.values())
    )
    critical: list[str] = []
    if parseability.score < 60:
        critical.append("Generated artifacts do not parse reliably enough.")
    if completeness.score < 60:
        critical.append("Required contact or work-history structure is incomplete.")
    if any(glyph in markdown for glyph in BAD_GLYPHS):
        critical.append("Markdown source contains corrupted characters.")

    final_disposition = disposition(overall, critical, targeted_complete)
    hashes = {
        "resume": sha256(args.resume),
        "docx": sha256(args.docx),
        "pdf": sha256(args.pdf),
    }
    if args.job:
        hashes["job"] = sha256(args.job)

    report = render_report(
        args,
        scores,
        overall,
        final_disposition,
        critical,
        requirement_rows,
        hashes,
        targeted_complete,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")

    machine_result = {
        "validator_version": VERSION,
        "overall_score": overall,
        "disposition": final_disposition,
        "targeted_complete": targeted_complete,
        "pass_number": args.pass_number,
        "categories": {
            name: {**asdict(category), "weight": weight}
            for name, (category, weight) in scores.items()
        },
        "critical_failures": critical,
        "hashes": hashes,
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(machine_result, indent=2) + "\n", encoding="utf-8")

    print(f"{overall} {final_disposition}")
    return 2 if critical else 0


if __name__ == "__main__":
    raise SystemExit(main())
