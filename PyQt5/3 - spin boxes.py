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
        self.label_1 = qtw.QLabel("Please Make Your Pick!")
        # Change label font size
        self.label_1.setFont(qtg.QFont("HYRunYuan", 24))
        self.layout().addWidget(self.label_1)

        # Create an spin box
        self.spin_1 = qtw.QDoubleSpinBox(self, 
                                         value = 10.0, 
                                         maximum = 20, 
                                         minimum = 0, 
                                         singleStep = 0.5,
                                         prefix = "# ",
                                         suffix = " Order")
        # Change font size
        self.spin_1.setFont(qtg.QFont("HYRunYuan", 24))
        # Put Combo Box on Screen
        self.layout().addWidget(self.spin_1)

        # Create a button
        self.button_1 = qtw.QPushButton("Press Me!", clicked = lambda: self.press_it())
        self.layout().addWidget(self.button_1)

        self.show()
    
    def press_it(self):
        self.label_1.setText(f"{self.spin_1.text()} is a good pick!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()