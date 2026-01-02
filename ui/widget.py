
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import QTimer
from ui.ui_widget import Ui_Widget 

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Radiation Exchange Simulator")
        
    # Connect sidebar buttons to stacked widget
        self.setup_connections()
        self.switch_page(0)  # Default to first page

    def setup_connections(self):
        # Dictionary mapping buttons to page index
        button_page_map = {
            self.geometryButton: 0,
            self.positioningButton: 5,
            self.meshingButton: 1,
            self.materialsButton: 2,
            self.simulationButton: 3,
            self.resultsButton: 4,
        }

        for button, page_index in button_page_map.items():
            button.clicked.connect(lambda checked, idx=page_index: self.switch_page(idx))

    def switch_page(self, index):
        """Switch stacked widget to the given page index"""
        self.stackedWidget.setCurrentIndex(index)
