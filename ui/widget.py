
from PySide6.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout, QLabel, QProgressBar
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap, QColor
from ui.ui_widget import Ui_Widget 
from controllers.stl_manager import STLManager
import os

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Radiation Exchange Simulator")
        
        # Connect sidebar buttons to stacked widget
        self.setup_connections()
        self.switch_page(0)  # Default to first page
            
        # Initialize STL Manager
        self.stl_manager = STLManager(self.vtkViewer) 
        
        # Connect buttons
        self.uploadFileAButton.clicked.connect(lambda: self.open_stl_file(1))
        self.uploadFileBButton.clicked.connect(lambda: self.open_stl_file(2))

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

    def open_stl_file(self, stl_number):
        dialog = QFileDialog(self)
        dialog.setNameFilter("STL Files (*.stl)")
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec():
            file_path = dialog.selectedFiles()[0]
            file_name = os.path.basename(file_path)

            # Validate STL
            valid = self.stl_manager.validate_stl(file_path)

            # Load STL if valid
            if valid:
                self.stl_manager.load_stl(file_path, stl_number)

            # Update individual STL UI
            if stl_number == 1:
                self.stl1_valid = valid
                icon_label = self.objectALoadedIcon
                text_label = self.objectALoadedLabel
            elif stl_number == 2:
                self.stl2_valid = valid
                icon_label = self.objectBLoadedIcon
                text_label = self.objectBLoadedLabel
            else:
                return

            # Update icon and label color
            if valid:
                icon_label.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
                text_label.setStyleSheet("color: #f1f5f9;")
                text_label.setText(f"{file_name} loaded")
                print(f"STL {stl_number} imported successfully")
            else:
                icon_label.setPixmap(QPixmap(":/icons/icons/warning_red.svg"))
                text_label.setStyleSheet("color: #ffa2a2;")
                print(f"STL {stl_number} import unsuccessful: No polygons found.")

            # --- Check if both STLs are loaded ---
            if getattr(self, "stl1_valid", False) and getattr(self, "stl2_valid", False):
                # Both loaded successfully
                self.readyPositioningIcon.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
                self.readyPositioningLabel.setStyleSheet("color: #f1f5f9;")
                self.statusLayout.setStyleSheet("background-color: #032e15; border-color: #7bf1a8; ")
                self.statusMessageLabel.setText("Both STL files loaded successfully. Ready for positioning!")
                self.statusMessageLabel.setStyleSheet("color: #7bf1a8;")
                self.statusIcon.setPixmap(QPixmap(":/icons/icons/check_green.svg"))
                print("Both STL files loaded successfully. Ready for positioning!")
            else:
                print("Not ready for positioning: One or both STLs missing.")
                self.statusMessageLabel.setText("Not ready for positioning: One or both STLs missing.")
