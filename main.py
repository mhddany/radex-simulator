import sys
from pathlib import Path
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon 
from ui.widget import Widget

app = QtWidgets.QApplication(sys.argv)

window = Widget()

BASE_DIR = Path(__file__).parent 
icon_path = BASE_DIR / "loader" / "tetrahedron.png"  # adjust if it's in a subfolder

window.setWindowIcon(QIcon(str(icon_path)))

window.show()

app.exec()