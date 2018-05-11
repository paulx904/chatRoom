import socket
import threading

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.sock.send(nickName.encode())
        print('Now Lets Chat, ',nickName)
        print(nickName,':')
    def sendThreadFunc(self):
        while True:
            try:
                myword = input()
                self.sock.send(myword.encode())
                #print(nickName,':')
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                if otherword:
                    print(otherword.decode())
                    print(nickName,':')
                else:
                    pass
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    c = Client('140.138.145.11', 8000)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

if __name__ == "__main__":
    print('Welcome to chat room!')
    nickName = input('input your nickname: ')
    main()
