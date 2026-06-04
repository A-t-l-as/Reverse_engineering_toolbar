Aod2Msh
*******

PL:

Włączamy program przez cmd. Komenda powinna wyglądać tak:
<ścieżka do aplikacji> <Nazwa modelu aod>.aod
Wciskamy enter i po sekundzie powinno robić msh z pliku aod. Pamiętaj, żeby w pliku aod była odpowiednia nazwa obiektu taka jak nazwa pliku aod.
Nazwa pliku aod = nazwa obiektu wewnatrz aod

Można również skorzystać z automatycznego systemu, który napisałem. Wystarczy wrzucić pliki .aod do katalogu input, a następnie
uruchomić _CONVERT_ALL.bat lub _CONVERT_ALL.ps1. W katalogu output po jakimś czasie powinny pojawić się pliki msh.

Można też skorzystać z wersji gui, ale to trzeba wejść do skryptu .py i zmienić ścieżkę w work_dir.

-----------------------------------------------------------------------------------------------------

EN:

We start the program via cmd. The command should look like this:
<path to the application> <AOD model name>.aod
Press Enter, and after a second, it should generate msh from the aod file. Remember to use the correct object name in the aod file, such as the name of the aod file.
Aod file name = object name inside aod

You can also use the automatic system I wrote. Just put the .aod files in the input directory, and then
run _CONVERT_ALL.bat or _CONVERT_ALL.ps1. After a while, msh files should appear in the output directory.

You can also use the GUI version, but you need to enter the .py script and change the path in work_dir.