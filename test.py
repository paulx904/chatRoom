from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import *
import example_ui
import sys
class Main(QMainWindow,example_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.send)
        self.pushButton_2.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
    def login(self):
        nickName=self.lineEdit.text()
        self.textBrowser.append("Welcome to chat room! "+nickName)
        self.textBrowser.update()
        self.textBrowser.append("Now Lets Chat, "+nickName)
        self.textBrowser.append("\n")
        self.textBrowser.update()
        self.lineEdit.setText("")
        self.pushButton.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
    def send(self):
        text=self.lineEdit_2.text()
        self.textBrowser.setAlignment(Qt.AlignRight)
        self.textBrowser.append(text)
        self.textBrowser.update()
        self.lineEdit_2.setText("")
if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())
