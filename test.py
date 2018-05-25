from PyQt5.QtWidgets import QMainWindow,QApplication
import example_ui
import sys

class Main(QMainWindow,example_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.pushButton.setText("Login")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.setText("send")
        self.pushButton_2.clicked.connect(self.send)

    def login(self):
        name=self.lineEdit.text()
        self.textBrowser.append(name)
        self.textBrowser.update()
        self.lineEdit.setText("")
        self.pushButton.setEnabled(False)
        self.lineEdit.setEnabled(False)

    def send(self):
        text=self.lineEdit_2.text()
        self.textBrowser.append(text)
        self.textBrowser.update()
        self.lineEdit_2.setText("")
if __name__=="__main__":
    app=QApplication(sys.argv)
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())
