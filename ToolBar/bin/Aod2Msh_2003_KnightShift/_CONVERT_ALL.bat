move .\input\*.aod .\

for %%i in (*.aod) do Aod2Msh.exe %%i

move .\*.aod .\input
move .\*.msh .\output

pause