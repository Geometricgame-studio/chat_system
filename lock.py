import os
import time

def asking(perr):
    os.system("cls")

    if perr:
        print("密碼錯誤!")

    a = input("輸入密碼 > ")

    if a == "12345":
        print("驗證成功! 請等待3秒...")
        time.sleep(3);
        os.system("cls")
        print("驗證成功!")
    elif a == "sleep":
        os.system("cls")
        print("螢幕即將休眠，按ENTER即可再次喚醒。")
        time.sleep(1)
        os.system("cls")
        input()

        asking(False)
    elif a == "exit":
        os.system("cls")
        print("Geometricgame System, press ENTER to login... > ")
        os.system("pause");
    
        asking(False)
    else:
        asking(True)

asking(False)