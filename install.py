import os
import zipfile

def pre_text(steps, errmsg = ""):
    os.system("cls")

    print("┏━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ GEOMETRICGAME APPS ┃")
    print("┃     App updater    ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━┛\n")
    print("更新進度", steps, "/ 5", errmsg)

pre_text(1)
print("正在檢查前置條件...")
try:
    import requests
except ModuleNotFoundError:
    print("正在安裝必要的模組 (1 / 1)")
    os.system("pip install requests")

    import requests

os.system('echo off')
os.system("cls")



pre_text(2)
print("正在連線至更新伺服器...")
print("連線時間由網路速度而定，請耐心等候!")
try:
    response = requests.get('https://drive.usercontent.google.com/u/0/uc?id=1UaVrItOYuk4k_ENwR9AtDIMa23XrYj12&export=download', stream=True)
except requests.exceptions.ConnectionError:
    pre_text(2, "- 連線錯誤!")
    print("錯誤 > 無法連線至更新伺服器!")
    exit()

total_size = int(response.headers.get("content-length", -1))
try:
    print("下載的版本 >", requests.get('https://freegeometricgames.com/last_version.txt').text, end="")
except:
    print("錯誤 > 無法取得安裝的版本")

print("更新檔案大小 >", round(total_size / 1024, 2), "MB")

pre_text(3)
print("正在下載更新...")
try:
    os.mkdir("C:\\GeometricgamesApps_update")
except:
    pass

with open("C:/GeometricgamesApps_update/update_datas.zip", 'wb') as f:
    f.write(response.content)
    
pre_text(4)
print("正在解壓縮更新檔案...")
import zipfile
with zipfile.ZipFile("C:/GeometricgamesApps_update/update_datas.zip", 'r') as zip_ref:
    zip_ref.extractall("C:/GeometricgamesApps_update/update_datas")

print("更新下載完成!")

pre_text(5)
path = "C:\\GeometricgamesApps_update\\update_datas\\net8.0-windows8.0\\All tools Form Apps.exe"
path = os.path.realpath(path)
os.startfile(path)
print("新的應用程式已開啟。")

os.system("exit")