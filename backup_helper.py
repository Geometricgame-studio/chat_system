import os
from os import listdir
from os.path import isfile, isdir, join
import time
import math


class FileCopier:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.total_size = os.path.getsize(source)
        
    def copy_file(self):
        try:
            with open(self.source, 'rb') as src, open(self.destination, 'wb') as dst:
                copied_size = 0
                start_time = time.time()
                
                while True:
                    buffer = src.read(1024 * 1024)
                    if not buffer:
                        break
                    dst.write(buffer)
                    copied_size += len(buffer)
                    
                    self.display_progress(copied_size, start_time)
        except PermissionError:
            pass

    def display_progress(self, copied_size, start_time):
        elapsed_time = time.time() - start_time
        speed = copied_size / (1024 * elapsed_time)
        progress_percentage = (copied_size / self.total_size) * 100
        
        print(f"\r進度: {progress_percentage:.2f}% | 檔案名稱: {os.path.basename(self.source)} | 速度: {speed:.2f} KB/s", end='')

if __name__ == "__main__":
    source_folder = "C:\\users\\ryanc\\"
    source_folder += input("輸入要複製的資料夾 > C:\\users\\ryanc\\")
    source_folder += "\\"
    print("要複製的資料夾:", source_folder)

    destination_file = input("選擇目的地 > ").replace('"', "")
    print("目的地資料夾:", destination_file)

    
    filenames = listdir(source_folder)
    print(filenames)
    
    for i in range(len(filenames)):
        persans = math.floor(i / len(filenames) * 100)
        print(f"\n整體進度: {persans}%")

        fullpath = join(source_folder, filenames[i])
        if isfile(fullpath):
            copier = FileCopier(source_folder + "\\" + filenames[i], destination_file + "\\" + filenames[i])
            copier.copy_file()
        elif isdir(fullpath):
            print("目前不支援資料夾類型的複製程序")

print("\n%s個檔案已備份完成!" % len(filenames))