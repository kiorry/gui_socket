import os

file_path = "./study_slice_file/13001.ksp"
file_size = os.stat(file_path).st_size


file_ = open(file_path,"rb")

mb = 1024 **2


print(file_size)
print(file_size/mb%9,"MB")

file_.close()