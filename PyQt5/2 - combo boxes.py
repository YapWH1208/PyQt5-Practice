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
        self.label_1.setFont(qtg.QFont("HYRunYuan", 18))
        self.layout().addWidget(self.label_1)

        # Create an combo box
        self.combo_1 = qtw.QComboBox(self, 
                                     # Making it editable
                                     editable=True, 
                                     insertPolicy=qtw.QComboBox.InsertAtTop)
        self.combo_1.addItem("One", "Choice One")
        self.combo_1.addItem("Two", 2)
        self.combo_1.addItem("Three", qtw.QWidget)
        self.combo_1.addItem("Four")
        self.combo_1.addItem("Five")
        self.combo_1.addItems(["1", "2", "3"])
        self.combo_1.insertItem(2, "One Thing")
        self.combo_1.insertItems(0, ["a", "b", " ", "c"])
        # Put Combo Box on Screen
        self.layout().addWidget(self.combo_1)

        # Create a button
        self.button_1 = qtw.QPushButton("Press Me!", clicked = lambda: self.press_it())
        self.layout().addWidget(self.button_1)

        self.show()
    
    def press_it(self):
        # To return text
        #self.label_1.setText(f"{self.combo_1.currentText()} is a good pick!")
        # To return data
        self.label_1.setText(f"{self.combo_1.currentData()} is a good pick!")
        # To return index
        #self.label_1.setText(f"{self.combo_1.currentIndex()} is a good pick!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()