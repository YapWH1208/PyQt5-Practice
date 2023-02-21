import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add Window Title
        self.setWindowTitle("PyQt5")

        # Set Form Layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add widgets
        self.label_1 = qtw.QLabel("Please Insert")
        self.label_1.setFont(qtg.QFont("HYRunYuan", 24))

        self.f_name = qtw.QLineEdit(self)
        self.l_name = qtw.QLineEdit(self)

        # Add rowa to app
        form_layout.addRow(self.label_1)
        form_layout.addRow("First Name", self.f_name)
        form_layout.addRow("Last Name", self.l_name)
        form_layout.addRow(qtw.QPushButton("Press Me!", clicked = lambda: self.press_it()))

        
        self.show()

    def press_it(self):
        self.label_1.setText(f"You pressed the button, {self.f_name.text()} {self.l_name.text()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()