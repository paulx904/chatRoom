from PyQt5.QtWidgets import QMainWindow, QApplication
import right_ui
import sys
import socket
import threading
from PyQt5.QtCore import *

class Client(QMainWindow, right_ui.Ui_loginButton):
    def __init__(self, host, port):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.send_button.clicked.connect(self.sendThreadFunc)#send_button是送出訊息的按鈕   pushButton是登入
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.pushButton.clicked.connect(self.send)
        self.send_button.setEnabled(False)
        self.send_text.setEnabled(False)#send_text是輸入訊息的欄位

    def sendThreadFunc(self):
        try:
            myword = self.send_text.text()
            self.sock.send(myword.encode())
            self.chaty.append(" ")
            myword = myword+" :You"
            self.chaty.setAlignment(Qt.AlignRight)
            self.chaty.append(myword)
            self.chaty.update()
            self.send_text.setText("")
        except ConnectionAbortedError:
            self.chaty.append('Server closed this connection!')
            self.chaty.update()
        except ConnectionResetError:
            self.chaty.append('Server is closed!')
            self.chaty.update()

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                self.chaty.append(otherword.decode())
                self.chaty.setAlignment(Qt.AlignLeft)
                self.chaty.update()
            except ConnectionAbortedError:
                self.chaty.append('Server closed this connection!')
            except ConnectionResetError:
                self.chaty.append('Server is closed!')


    def send(self):#11
        name = self.nickName.text()#nicknamet是暱稱
        self.sock.send(name.encode())
        self.chaty.update()
        self.nickName.setText("")
        self.send_text.setEnabled(True)
        self.send_button.setEnabled(True)
        self.pushButton.setEnabled(False)
        self.nickName.setEnabled(False)
        self.password.setEnabled(False)
        th2 = threading.Thread(target=self.recvThreadFunc)
        th2.setDaemon(True)
        th2.start()


def main():
    c = Client('140.138.145.20', 8000)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Client('140.138.145.20', 8000)
    MainWindow.show()
    sys.exit(app.exec_())
    main()
