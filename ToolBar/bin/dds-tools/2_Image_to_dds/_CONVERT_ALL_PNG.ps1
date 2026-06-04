$folderPath = ".\" 

$pngFiles = Get-ChildItem -Path $folderPath -Filter "*.png"

foreach ($file in $pngFiles)
{
    Write-Output "File processing: $($file.FullName)"
    .\texconv.exe $file
}

 Write-Host "Press Enter to continue..."
 Read-Host