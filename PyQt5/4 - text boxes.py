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

        # Create an text box
        self.text_1 = qtw.QTextEdit(self,
                                    #html = "<h3> This is a HEADER </h3>",
                                    #plainText = "This is real",
                                    acceptRichText = False, # Text with formats
                                    lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
                                    lineWrapColumnOrWidth = 50,
                                    placeholderText = "Insert Here",
                                    readOnly = False)
        # Change font size
        self.text_1.setFont(qtg.QFont("HYRunYuan", 24))
        # Put Combo Box on Screen
        self.layout().addWidget(self.text_1)

        # Create a button
        self.button_1 = qtw.QPushButton("Press Me!", clicked = lambda: self.press_it())
        self.layout().addWidget(self.button_1)

        self.show()
    
    def press_it(self):
        self.label_1.setText(f"You insert {self.text_1.toPlainText()}")
        self.text_1.setPlainText("")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()