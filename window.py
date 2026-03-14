from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from gui import Ui_MainWindow
from version import version
from kicad_pcb import KiCadPCB

IU_PER_MM = 1000000
IU_PER_MILS = 25400

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Track Optimizer v{version}")
        self.pcb = KiCadPCB()

        self.unit: int = IU_PER_MILS
        self.ui.editWidth.setText("8.0")
        self.ui.editGap.setText("8.0")
        self.ui.editLength.setText("60.0")
        self.ui.comboMode.addItems(["Perpendicular", "0 Degrees", "22.5 Degrees", "45 Degrees", "67.5 Degrees", "90 Degrees", "-22.5 Degrees", "-45 Degrees", "-67.5 Degrees", "-90 Degrees"])
        self.ui.radioRemove.setChecked(True)
        self.ui.radioMil.setChecked(True)
        self.ui.radioMil.toggled.connect(self.on_unit_changed)
        self.ui.buttonClose.clicked.connect(self.close)
        self.ui.buttonConnect.clicked.connect(self.load_initial_data)
        self.ui.buttonRun.clicked.connect(self.button_run_clicked)
        self.ui.buttonBreakout.clicked.connect(self.button_breakout_clicked)
        QTimer.singleShot(500, self.load_initial_data)
    
    def load_initial_data(self):
        connected, status = self.pcb.connect_kicad()
        if connected:
            self.ui.statusbar.showMessage(f"Connected to KiCad {self.pcb.kicad.get_version()}")
            print(f"Connected to KiCad {self.pcb.kicad.get_version()}")
            print(f"Opening file {self.pcb.board.document.board_filename}")
        else:
            self.ui.statusbar.showMessage(status)
            QMessageBox.information(self, "Message", status)

    def button_run_clicked(self):
        check_remove = self.ui.radioRemove.isChecked()
        check_merg = self.ui.radioMerg.isChecked()
        check_total = self.ui.radioTotal.isChecked()
        if check_remove:
            print("Remove stubs track")
            self.pcb.remove_stubs_recursive()
        if check_merg:
            print("Merging collinear tracks")
            self.pcb.merge_overlapping_tracks()
        if check_total:
            print("Remove stubs track & Merging collinear tracks")
            self.pcb.remove_stubs_recursive()
            self.pcb.merge_overlapping_tracks()

    def button_breakout_clicked(self):
        width = int(self.unit*parse_float(self.ui.editWidth.text()))
        gap = int(self.unit*parse_float(self.ui.editGap.text()))
        escape_length = int(self.unit*parse_float(self.ui.editLength.text()))
        flip = self.ui.checkFlip.isChecked()
        mode = self.ui.comboMode.currentText()
        status = self.pcb.breakout_diff_pair(width, gap, escape_length, mode, flip)
        if status == 2:
            QMessageBox.information(self, "Message", "Please select exactly 2 pads before running this tool")

    def on_unit_changed(self):
        check = self.ui.radioMil.isChecked()
        self.change_unit(check)
        if check:
            self.unit = IU_PER_MILS
        else:
            self.unit = IU_PER_MM

    def change_unit(self, uint: bool):
        width = parse_float(self.ui.editWidth.text())
        if width == None:
            QMessageBox.information(self, "Error", "Error: Invalid Differential Pair Width")
            return
        gap = parse_float(self.ui.editGap.text())
        if gap == None:
            QMessageBox.information(self, "Error", "Error: Invalid Differential Pair Gap")
            return
        length = parse_float(self.ui.editLength.text())
        if length == None:
            QMessageBox.information(self, "Error", "Error: Invalid Escape Length")
            return
        if uint:
            self.ui.editWidth.setText(f"{width*IU_PER_MM/IU_PER_MILS}")
            self.ui.editGap.setText(f"{gap*IU_PER_MM/IU_PER_MILS}")
            self.ui.editLength.setText(f"{length*IU_PER_MM/IU_PER_MILS}")
        else:
            self.ui.editWidth.setText(f"{width*IU_PER_MILS/IU_PER_MM}")
            self.ui.editGap.setText(f"{gap*IU_PER_MILS/IU_PER_MM}")
            self.ui.editLength.setText(f"{length*IU_PER_MILS/IU_PER_MM}")
            
def parse_float(text: str) -> float | None:
    try:
        clean_text = text.replace(',', '.').strip()
        return float(clean_text)
    except ValueError:
        return None
