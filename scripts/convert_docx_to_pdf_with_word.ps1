param(
    [Parameter(Mandatory = $true)]
    [string]$DocxPath
)

$ErrorActionPreference = 'Stop'
$word = $null
$document = $null

try {
    $resolvedDocx = (Resolve-Path -LiteralPath $DocxPath).Path
    $pdfPath = [System.IO.Path]::ChangeExtension($resolvedDocx, '.pdf')

    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0

    $document = $word.Documents.Open($resolvedDocx, $false, $true)
    $document.ExportAsFixedFormat($pdfPath, 17)
}
finally {
    if ($null -ne $document) {
        $document.Close(0)
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($document)
    }
    if ($null -ne $word) {
        $word.Quit()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($word)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}
