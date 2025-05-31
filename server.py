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

print("伺服器已啟動，在 >", socket.gethostbyname(socket.gethostname()))

s.listen(port)

sockets = []

def send_all(response):
    try:
        for i in sockets:
            try:
                i.send(response)
            except ValueError:
                sockets.remove(i)
                print("已移除", i)
    except ConnectionResetError:
        print("客戶端已中斷連線。")


def handle_client(client_socket, ips, ports):
    sockets.append(client_socket)

    while True:
        try:
            request = client_socket.recv(9999999)
            print("接收到訊息 >", request.decode())

            print("現有的客戶端 >", len(sockets))
            send_all(request)
        except ConnectionResetError:
            print("%s:%d" % (ips, ports), "已中斷連線。")
        except UnicodeDecodeError:
            send_all(request)


while True:
    c, a = s.accept()
    
    print("%s:%d" % (a[0], a[1]), "已從遠端連線。")

    client_handler = threading.Thread(target=handle_client, args=(c, a[0], a[1]))
    client_handler.start()

    print("待機中...")