import os;
try:
    os.system('cls')
    print("正在檢查必要的模組...")
    from PIL import Image, ImageSequence
    import tkinter as tk
    from tkinter import filedialog
except ModuleNotFoundError:
    os.system('cls')
    print("正在安裝必要的模組 [1 / 2]")
    os.system('pip install pillow')
    os.system('cls')
    print("正在安裝必要的模組 [2 / 2]")
    os.system('pip install tk')
    os.system('cls')
    from PIL import Image, ImageSequence
    import tkinter as tk
    from tkinter import filedialog
os.system('cls')
print("正在選擇圖片或GIF檔案...\n請勿關閉此視窗!")
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
os.system('cls')

if not(filename):
    print("請求已取消")
    exit()

input_path = filename
output_path_clean = "" + str(os.path.dirname(filename)) + "/" + str(os.path.splitext(os.path.basename(filename))[0]) + " (No Background)" + str(os.path.splitext(os.path.basename(filename))[1])

try:
    im = Image.open(input_path)

    progress = 0
    frames = []

    for frame in ImageSequence.Iterator(im):
        frame = frame.convert("RGBA")
        datas = frame.getdata()
        new_data = []
        for item in datas:
            # Use a wider tolerance for black shades to clean more thoroughly
            if item[0] < 80 and item[1] < 80 and item[2] < 80:
                new_data.append((0, 0, 0, 0))
            else:
                new_data.append(item)
        frame.putdata(new_data)
        frames.append(frame)
        progress += 1
        print("已完成: %s%s" % (round(progress / im.n_frames * 100, 1), "%"), end="\r")
except:
    print("選擇的檔案並非圖檔或GIF檔")
    exit()

# Save cleaned transparent background GIF
print('正在儲存檔案...')
frames[0].save(output_path_clean, save_all=True, append_images=frames[1:], loop=0, disposal=2, transparency=0)

output_path_clean

os.system('cls')
print("完成!")
print("檔案已匯出至: %s" % output_path_clean)