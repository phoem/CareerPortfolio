#!/usr/bin/env python3
"""Generate DOCX and PDF artifacts from canonical resume Markdown files."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
SOURCE_GLOBS = ("generic/*.md", "netflix/*.md")


def add_bottom_border(paragraph) -> None:
    properties = paragraph._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "5")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "666666")
    borders.append(bottom)
    properties.append(borders)


def add_inline_markup(paragraph, text: str) -> None:
    for part in re.split(r"(\*\*.*?\*\*|\*.*?\*)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            paragraph.add_run(part)


def markdown_to_docx(source: Path, destination: Path) -> None:
    is_letter = "Cover_Letter" in source.name
    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(0.65 if is_letter else 0.42)
    section.bottom_margin = Inches(0.65 if is_letter else 0.42)
    section.left_margin = Inches(0.75 if is_letter else 0.52)
    section.right_margin = Inches(0.75 if is_letter else 0.52)

    normal = document.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10.5 if is_letter else 8.7)
    normal.paragraph_format.space_after = Pt(5 if is_letter else 1.2)
    normal.paragraph_format.line_spacing = 1.08 if is_letter else 1.0

    for style_name, size in (("Heading 1", 11.2), ("Heading 2", 10.0), ("Heading 3", 9.2)):
        style = document.styles[style_name]
        style.font.name = "Arial"
        style.font.bold = True
        style.font.size = Pt(size)
        style.paragraph_format.space_before = Pt(3)
        style.paragraph_format.space_after = Pt(1)
        style.paragraph_format.keep_with_next = True

    for line in source.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if line.startswith("# "):
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_after = Pt(0)
            title = line[2:]
            if title.startswith("Jordan Newman -"):
                title = "JORDAN NEWMAN"
            run = paragraph.add_run(title)
            run.bold = True
            run.font.size = Pt(15 if is_letter else 16)
        elif line.startswith("## "):
            paragraph = document.add_paragraph(style="Heading 1")
            paragraph.add_run(line[3:].upper())
            add_bottom_border(paragraph)
        elif line.startswith("### "):
            paragraph = document.add_paragraph(style="Heading 2")
            paragraph.add_run(line[4:])
        elif line.startswith("- "):
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.left_indent = Inches(0.16)
            paragraph.paragraph_format.first_line_indent = Inches(-0.12)
            paragraph.paragraph_format.space_after = Pt(0.8)
            paragraph.add_run("• ").bold = True
            add_inline_markup(paragraph, line[2:])
        elif line.startswith("**") and line.endswith("**"):
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT if is_letter else WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_after = Pt(0)
            run = paragraph.add_run(line[2:-2])
            run.bold = True
            run.font.size = Pt(10.2)
        elif line.startswith("*") and line.endswith("*"):
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.add_run(line[1:-1]).italic = True
        else:
            paragraph = document.add_paragraph()
            if not is_letter and line.startswith("Marlboro, NJ"):
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                paragraph.paragraph_format.space_after = Pt(2)
            add_inline_markup(paragraph, line)

    footer = document.sections[0].footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Jordan Newman").font.size = Pt(7)
    document.save(destination)


def convert_to_pdf(docx_path: Path) -> None:
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(docx_path.parent),
            str(docx_path),
        ],
        check=True,
    )


def main() -> None:
    sources: list[Path] = []
    for pattern in SOURCE_GLOBS:
        sources.extend(sorted(ROOT.glob(pattern)))

    for source in sources:
        destination = source.with_suffix(".docx")
        markdown_to_docx(source, destination)
        convert_to_pdf(destination)
        print(f"Generated {destination.relative_to(ROOT)} and {destination.with_suffix('.pdf').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
