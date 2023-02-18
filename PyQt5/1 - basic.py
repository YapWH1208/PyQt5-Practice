import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add Window Title
        self.setWindowTitle("PyQt5")

        # Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a Label
        self.label_1 = qtw.QLabel("Hello World!")
        # Change label font size
        self.label_1.setFont(qtg.QFont("HYRunYuan", 18))
        self.layout().addWidget(self.label_1)

        # Create an entry box
        self.entry_1 = qtw.QLineEdit()
        self.entry_1.setObjectName("name_field")
        self.entry_1.setText("")
        self.layout().addWidget(self.entry_1)

        # Create a button
        self.button_1 = qtw.QPushButton("Press Me!", clicked = lambda: self.press_it())
        self.layout().addWidget(self.button_1)

        self.show()
    
    def press_it(self):
        self.label_1.setText(f"Hello {self.entry_1.text()}!")
        self.entry_1.setText("")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()