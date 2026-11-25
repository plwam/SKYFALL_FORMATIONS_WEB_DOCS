# Finalise le livrable : copie du PDF, creation de l'archive et controle.
$ErrorActionPreference = "Stop"
$src = "D:\smarta\gesi formation\module-django-gesibiblio"
$out = "D:\smarta\gesi formation"
$zip = Join-Path $out "Module_Django_GesiBiblio.zip"
$pdf = Join-Path $out "Module_Django_GesiBiblio.pdf"

if (-not (Test-Path (Join-Path $src "main.pdf"))) {
    throw "main.pdf absent : compilez d'abord main.tex."
}

Copy-Item (Join-Path $src "main.pdf") $pdf -Force
if (Test-Path $zip) { Remove-Item $zip -Force }

Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$excludeFiles = @(
    "main.aux", "main.log", "main.out", "main.toc", "main.xdv",
    "_compile.log", "main.synctex.gz",
    "main-rapide.pdf", "main-rapide.aux", "main-rapide.log",
    "main-rapide.out", "main-rapide.toc", "main-rapide.xdv",
    "_rapide.log"
)
$excludeDir = @("_outils")

$archive = [System.IO.Compression.ZipFile]::Open(
    $zip, [System.IO.Compression.ZipArchiveMode]::Create
)
try {
    Get-ChildItem $src -Recurse -File | ForEach-Object {
        $rel = $_.FullName.Substring($src.Length + 1).Replace("\", "/")
        $name = $_.Name
        $skip = $false
        if ($name -like "_test*") { $skip = $true }
        if ($excludeFiles -contains $name) { $skip = $true }
        foreach ($d in $excludeDir) {
            if ($rel -like "$d/*") { $skip = $true }
        }
        if (-not $skip) {
            $entry = $rel.Replace("\", "/")
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                $archive, $_.FullName, $entry,
                [System.IO.Compression.CompressionLevel]::Optimal
            ) | Out-Null
        }
    }
}
finally {
    $archive.Dispose()
}

"Archive creee : $zip"
"Taille : {0:N2} Mo" -f ((Get-Item $zip).Length / 1MB)
"PDF copie : $pdf"
"Entrees :"
$read = [System.IO.Compression.ZipFile]::OpenRead($zip)
try {
    $read.Entries | Sort-Object FullName | ForEach-Object {
        "  {0,10}  {1}" -f $_.Length, $_.FullName
    }
}
finally {
    $read.Dispose()
}
