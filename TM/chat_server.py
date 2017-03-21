#server
import socket
import time
import threading


def tcplink(sock, addr):
    global socks
    socks.append(sock)
    print('Accept new connection from %s:%s' % addr)
    sock.send('Welcome!'.encode())
    while True:
        data = sock.recv(1024).decode()
        print(data)
        time.sleep(0.1)
        if data.split(':')[1] == 'exit':
            print('break')
            break
        #sock.send(('Hello, %s!' % data).encode())
        for i in socks:
            if i != sock:
                i.send(data.encode())
    sock.close()
    socks.remove(sock)
    print('Connection from %s:%s closed.' % addr)

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
threads = []
global socks
socks = []
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()