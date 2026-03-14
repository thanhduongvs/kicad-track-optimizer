from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from gui import Ui_MainWindow
from version import version
from kicad_pcb import KiCadPCB

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Track Optimizer v{version}")
        self.pcb = KiCadPCB()

        self.ui.radioRemove.setChecked(True)
        self.ui.buttonClose.clicked.connect(self.close)
        self.ui.buttonConnect.clicked.connect(self.load_initial_data)
        self.ui.buttonRun.clicked.connect(self.button_run_clicked)

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