import socket
import os
import threading
import time

#Startup settings
try:
    os.system("mkdir C:\\py_chat\\downloads")
except FileExistsError:
    pass

#connect infos
os.system("cls")
ip = input("聊天伺服器IP地址 (預設 127.0.0.1) > ") or "127.0.0.1"
port = int(input("聊天伺服器Port (預設 5000) > ") or 5000)

user_name = input("輸入您的暱稱 > ")

#connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system("cls")
print("正在連線到 %s" % ip)

def exit_client():
    exit()

def is_text_file(res):
    try:
        res.decode()
        return True
    except UnicodeDecodeError:
        return False

last_info = ""
def message_action():
    try:
        while True:
            response = s.recv(9999999)

            #known response type
            info = ""
            if is_text_file(response):
                #check info response
                if "infos:" in response.decode():
                    infor = response.decode().split(':')[1]
                    info = infor
                    global last_info
                    last_info = info
                elif "connecturl:" in response.decode():
                    curlcmd = "curl "
                    curlcmd += response.decode().split(':')[1]
                    os.system(curlcmd)
                else:
                    print(response.decode())
            else:
                print("正在下載 >", last_info)

                fullpath = "C:\\py_chat\\downloads\\"
                fullpath += last_info
                with open(fullpath, "wb") as binary_file:
                    binary_file.write(response)

                print("檔案下載完成，路徑 >", fullpath)

            time.sleep(0.5)

            if stop_thread:
                break
    except ConnectionResetError:
        os.system("cls")
        print("失去連線")
        print("遠端主機已強制關閉一個現存的連線。")
        exit_client()
        exit()
    except ConnectionAbortedError:
        os.system("cls")
        print("失去連線")
        print("連線已被您主機上的軟體中止。")
        exit()
stop_thread = False

def read_cmd(commands):
    cmd = str(commands.split(':')[1])

    if cmd == "file":
        patho = input("輸入檔案地址 > ")
        path = patho.replace('"', "")

        print("從", path, "讀取檔案...")
        f = open(path, 'rb')
        bin = f.read()
        f.close()

        msg = user_name
        msg += " 傳送了檔案 > " + os.path.basename(path).split('/')[-1]
        s.send(msg.encode())

        time.sleep(0.5)
        infomsg = "infos:"
        infomsg += os.path.basename(path).split('/')[-1]
        s.send(infomsg.encode())
        s.send(bin)

        print("檔案已發送")
    elif cmd == "url":
        urls = input("輸入要連線的網址 > ")
        infomsg = "connecturl:"
        infomsg += urls
        s.send(infomsg.encode())

        msg = user_name
        msg += " 傳送了一個連結"
        s.send(msg.encode())

        print("連線資訊已發送")
    else:
        print("未知的指令 >", cmd)

try:
    s.connect((ip, port))
    os.system("cls")
    print("您已成功加入 > %s" % ip)

    msg = user_name
    msg += " 加入了聊天室"
    s.send(msg.encode())

    msg_printer = threading.Thread(target=message_action, args=())
    msg_printer.start()

    while True:
        g = input("")

        #doing command
        if ("command:" in g):
            read_cmd(g)
        else:
            msg = user_name
            msg += " 說 > "
            msg += g
            s.send(msg.encode())
except ConnectionResetError:
    os.system("cls")
    print("失去連線")
    print("遠端主機已強制關閉一個現存的連線。")
    exit()
except ConnectionRefusedError:
    os.system("cls")
    print("連線失敗")
    print(ip, "拒絕連線。")
    exit()
except TimeoutError:
    os.system("cls")
    print("連線失敗")
    print(ip, "連線逾時。")
    exit()
except socket.gaierror:
    os.system("cls")
    print("連線失敗")
    print(ip, "不符合標準格式。")
    exit()
except OSError:
    os.system("cls")
    print("系統錯誤")
    exit()
except ConnectionAbortedError:
    os.system("cls")
    print("失去連線")
    print("連線已被您主機上的軟體中止。")
    exit()