import os
import time

def start(sec):
    left = sec
    while left > 0:
        os.system("cls")
        print(left)
        left -= 1
        time.sleep(1)

    os.system("cls")
    print("時間到!")

    opt = input("選項: R - 重新計時 | T - 變更秒數 | 其他 - 結束 > ")

    if opt == "r":
        start(sec)
    elif opt == "t":
        try:
            start(int(input("輸入秒數 > ")))
        except:
            start(0)

    os.system("cls")

try:
    start(int(input("輸入秒數 > ")))
except:
    start(0)