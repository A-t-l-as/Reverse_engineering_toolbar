mv .\input\*.aod .\

$folderPath = ".\"

# Get all .aod files in the folder
$aodFiles = Get-ChildItem -Path $folderPath -Filter "*.aod"

foreach ($file in $aodFiles)
{
    Write-Output "File processing: $($file.FullName)"
    .\Aod2Msh.exe $file
}

mv .\*.aod .\input
mv .\*.msh .\output

 Write-Host "Press Enter to continue..."
 Read-Host