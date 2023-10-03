import PyQt5.QtWidgets as QtWidgets

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
window.setWindowTitle('Radio Button Example')

layout = QtWidgets.QVBoxLayout()

radio_button1 = QtWidgets.QRadioButton("Option 1")
radio_button2 = QtWidgets.QRadioButton("Option 2")
radio_button3 = QtWidgets.QRadioButton("Option 3")

layout.addWidget(radio_button1)
layout.addWidget(radio_button2)
layout.addWidget(radio_button3)

window.setLayout(layout)

window.show()

app.exec()