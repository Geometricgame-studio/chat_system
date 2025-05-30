import socket
import threading
import os
import sys

os.system("cls")
os.system("title 伺服器端")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5000
try:
    s.bind(("127.0.0.1", port))
except OSError:
    print("伺服器已經在另一個地方啟動，請先關閉該伺服器再重新啟動此程式。")
    os.system("pause")
    os.execv(sys.executable, ['python'] + sys.argv)

print("伺服器已啟動")

s.listen(port)

sockets = []
def handle_client(client_socket, ips, ports):
    sockets.append(client_socket)

    while True:
        try:
            request = client_socket.recv(9999999)
            print("接收到訊息 >", request.decode())

            print("現有的客戶端 >", len(sockets))
            for i in sockets:
                i.send(request)
        except ConnectionResetError:
            print("%s:%d" % (ips, ports), "已中斷連線。")
            sockets.remove(client_socket)
        except UnicodeDecodeError:
            print("收到無法解讀的訊息，可能是一個檔案")
            try:
                for i in sockets:
                    i.send(request)
            except ConnectionResetError:
                print("%s:%d" % (ips, ports), "已中斷連線。")
                sockets.remove(client_socket)


while True:
    c, a = s.accept()
    
    print("%s:%d" % (a[0], a[1]), "已從遠端連線。")

    client_handler = threading.Thread(target=handle_client, args=(c, a[0], a[1]))
    client_handler.start()

    print("待機中...")