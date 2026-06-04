import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import Qt


# Lista aplikacji: nazwa + polecenie systemowe
apps = {
    "Run KnightShift game": "start PATH/TO/KS/KnightShift.exe" if sys.platform == "win32" else "brave",
    "Notepad": "start notepad++" if sys.platform == "win32" else "gedit",
    "Calc": "calc" if sys.platform == "win32" else "gnome-calculator",
    "Hex Editor": "start hxd" if sys.platform == "win32" else "brave",
    "TexViewer": "python ./bin/TexViewer/texviewgui.py" if sys.platform == "win32" else "brave",
    "GimmickTexViewer": "python ./bin/GimmickTexViewer/Tex2PicViewerGui.py" if sys.platform == "win32" else "brave",
    "Run WDPack 081 (Blue)": "start PATH/TO/WDPACK/WDPack.exe" if sys.platform == "win32" else "brave",
    "Run WDPackager (Yellow)": "start PATH/TO/WDPACKAGER/WDPackager.exe" if sys.platform == "win32" else "brave",
    "Export WD with EarthToolCli": "python ./bin/EarthTool/EarthToolCliGui.py" if sys.platform == "win32" else "brave",
    "LanEditor": "start ./bin/LanEditor/LanEditor.exe" if sys.platform == "win32" else "brave",
    "Export wavepack (.wpk) to .cpp": "python ./bin/WpkExporter/WpkExportToCpp.py" if sys.platform == "win32" else "brave",
    "Export wavepack (.wpk) to .txt": "python ./bin/WpkExporter/WpkExportToTxt.py" if sys.platform == "win32" else "brave",
    "Convert .txt/.cpp to wavepack": "python ./bin/WpkImporter/WpkImporterGui.py" if sys.platform == "win32" else "brave",
    "Convert audio to .tws": "python ./bin/ConvertToTws/ConvertToTws.py" if sys.platform == "win32" else "brave",
    "Repair map file name": "python ./bin/Repair_name_in_map_file/repair_single_file.py" if sys.platform == "win32" else "brave",
    "Delete ! from campaign map file": "python ./bin/Repair_name_in_map_file/repair_single_file.py" if sys.platform == "win32" else "brave",
    "Convert .png to .bmp grayscale": "python ./bin/Png_to_grayscale_gui/Png_to_grayscale_gui.py" if sys.platform == "win32" else "brave",
    "Apply a border to the map bitmap": "python ./bin/Apply_border_script_gui/Apply_border_script_gui.py" if sys.platform == "win32" else "brave",
    "Run KnightShift-DeveloperEditor": "start KS/DEV/EDITOR/PATH/KnightShift-DeveloperEditor.exe" if sys.platform == "win32" else "brave",
    "Edit EditorDef.txt": "start notepad++ ./sample_work_space/Parameters/EditorDef.txt" if sys.platform == "win32" else "brave",
    "Decompress the zlib file": "python ./bin/Decompress_zlib/DecompressZlib.py" if sys.platform == "win32" else "brave",
    "Decompress map file": "python ./bin/MapExtractor/MapExtractorGui2.py" if sys.platform == "win32" else "brave",
    "Compress data directory to map": "python ./bin/MapPackager/MapPackagerGui.py" if sys.platform == "win32" else "brave",
    
    "Decompile map by KsMapDecompiler": "java -jar ./bin/KsMapDecompiler/KsMapDecompiler.jar" if sys.platform == "win32" else "brave",
    "Compile map by KsMapCompiler": "python ./bin/KsMapCompiler/start.py" if sys.platform == "win32" else "brave",
    "Edit GameModes.cfg": "start notepad++ ./GameModes.cfg" if sys.platform == "win32" else "brave",
    
    "Go to ParTool": "python ./bin/GoTo/GoToParTool.py" if sys.platform == "win32" else "brave",
    "Go to the .par working directory.": "python ./bin/GoTo/GoToParDir.py" if sys.platform == "win32" else "brave",
    "Compile .par file.": "python ./bin/Turbo-ParTool-ByAtlas_v5_0/PARim/IMPORT_SCRIPT.py" if sys.platform == "win32" else "brave",
    
    "Convert .msh to .prt": "python ./bin/ParticleTool/ConvertMshToPrt.py" if sys.platform == "win32" else "brave",
    "Convert .prt to .msh": "python ./bin/ParticleTool/ConvertPrtToMsh.py" if sys.platform == "win32" else "brave",
    "Export .msh particle to .myaod": "python ./bin/ParticleTool/ExportMshToMyAod.py" if sys.platform == "win32" else "brave",
    "Import particle directory to .msh": "python ./bin/ParticleTool/ImportMyAodToMsh.py" if sys.platform == "win32" else "brave",
    "Edit DynamicParticle.cfg": "start notepad++ ./DynamicParticle.cfg" if sys.platform == "win32" else "brave",
    "ParticleEdit Earth 2160": "start ./bin/Particle_Edit_Earth2160/ParticleEdit_SSE.exe" if sys.platform == "win32" else "brave",
    "Convert .aod to .msh": "python ./bin/Aod2Msh_2003_KnightShift/Aod2MshGui.py" if sys.platform == "win32" else "brave",
    "Go to Aod2Msh directory": "python ./bin/GoTo/GoToAod2Msh.py" if sys.platform == "win32" else "brave",
    "Go to Scripts directory": "python ./bin/GoTo/GoToScripts.py" if sys.platform == "win32" else "brave",
    "Run EarthCdbg": "start ./bin/EarthCdbg/EarthCdbg.exe" if sys.platform == "win32" else "brave",
    "DDS Texture Viewer": "start ./bin/dds-tools/1_Windows_dds_tex_viewer/WTV/WTV.exe" if sys.platform == "win32" else "brave",
    "Go to dds-tools directory": "python ./bin/GoTo/GoToDDSTools.py" if sys.platform == "win32" else "brave",
}

class Toolbar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout główny
        main_layout = QVBoxLayout(self)

        # Scroll area
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        # Widget w środku scrolla
        container = QWidget()
        layout = QVBoxLayout(container)

        # Dodajemy przyciski
        for name, command in apps.items():
            btn = QPushButton(name)
            btn.clicked.connect(lambda _, cmd=command: self.run_app(cmd))
            layout.addWidget(btn)

        container.setLayout(layout)
        scroll.setWidget(container)

        # Dodajemy scrolla do głównego layoutu
        main_layout.addWidget(scroll)

        self.setLayout(main_layout)
        self.setWindowTitle("KnightShift SDK ToolBar")
        self.setFixedWidth(250)  # trochę szersze dla czytelności
        self.setFixedHeight(500) # ograniczona wysokość -> scroll działa
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Tool)

    def run_app(self, command):
        try:
            if sys.platform == "win32":
                subprocess.Popen(command, shell=True)
            else:
                subprocess.Popen(command.split())
        except Exception as e:
            print(f"Nie udało się uruchomić {command}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    toolbar = Toolbar()
    toolbar.show()
    sys.exit(app.exec_())