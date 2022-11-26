import os
import shutil

os.mkdir("My_PYTHON")
src = "folder.txt"
src1 = "folder1.txt"
src2 = "folder2.txt"
dst = "My_PYTHON/"
check_file = os.path.exists(src)
check_file1 = os.path.exists(src1)
check_file2 = os.path.exists(src2)
if check_file:
    shutil.copy(src, dst)
else:
    print("Вихідний файл відсутній!")
if check_file1:
    shutil.copy(src1, dst)
else:
    print("Вихідний файл відсутній!")

if check_file2:
    shutil.copy(src2, dst)
else:
    print("Вихідний файл відсутній!")
