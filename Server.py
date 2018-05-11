# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, strftime
import datetime
x = datetime.datetime.now() #現在時間
x.hour   #時
x.minute #分
x.second #秒 59

class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.mydict = dict()
        self.count =0

    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())

        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                #connection.send(b'welcome to chat room!')
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()
                print('Welcome to chat room!')
            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass


    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    c.send(whatToSay.encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        nickname = myconnection.recv(1024).decode()
        self.mydict[myconnection.fileno()] = nickname
        self.mylist.append(myconnection)
        self.count=self.count+1
        print('connection', connNumber, ' has nickname :', nickname)
        self.tellOthers(connNumber, '【hint：'+self.mydict[connNumber]+' in the chat room】')
        self.tellOthers(connNumber, '【hint：'+ str(self.count)+'  people in chat room】')
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    print(self.mydict[connNumber], ':', recvedMsg)
                    self.tellOthers(connNumber, self.mydict[connNumber]+' :'+recvedMsg+'\t'+'['+str(x.hour)+':'+str(x.minute)+':'+str(x.second)+']')
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                except:
                    pass

                print(self.mydict[connNumber], 'exit, ', len(self.mylist), ' person left')
                self.tellOthers(connNumber, '【[hint]：'+self.mydict[connNumber]+' leave the chat room.】')
                self.count= self.count-1
                self.tellOthers(connNumber, '【hint：'+ str(self.count)+'  people in chat room】')
                myconnection.close()
                return


def main():
    s = Server('140.138.145.11', 8000)
    #print('Welcome to chat room!')
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

