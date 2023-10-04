from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

def button_clicked():
    text = text_box.text()
    print("Button Clicked! Text:", text)


def job_icon_button():
    button = QPushButton(window)
    button.setGeometry(100, 50, 100, 100)
    icon=QIcon('./colored_icons/bard.png')
    pixmap = icon.pixmap(QSize(100, 100))
    button.setIcon(QIcon(pixmap))
    button.setIconSize(pixmap.size())
    button.clicked.connect(button_clicked)



app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My Window")
window.setGeometry(100, 100, 300, 200)

text_box = QLineEdit(window)
text_box.setGeometry(100, 100, 100, 30)
job_icon_button()
job_icon_button()

window.show()
sys.exit(app.exec())