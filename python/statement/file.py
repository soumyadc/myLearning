#!/usr/bin/python

# Open a file

def open_tmp_file(file_name, mode):
    fo = open(file_name, mode)
    print ("Name of the file: ", fo.name)
    print ("Closed or not : ", fo.closed)
    print ("Opening mode : ", fo.mode)
    return fo

def close_tmp_file(file_obj):
    if file_obj.closed == False :
        file_obj.close()
        print("File Closed")
    return

def write_tmp_file(file_obj, w_buf):
    file_obj.write(w_buf)
    return

def read_tmp_file(file_obj, count):
    str = file_obj.read(count)
    return str

def check_current_pos(file_obj):
    pos=file_obj.tell()
    print("Current pos: ", pos)
    return pos

def seek_tmp_file():
    pos= fo.seek(0, 0) # seek(0,0) position to bigining of the file
    return pos




#file_name = input("Enter a filename: ")
#w_buf = input("What you want to write: ")

fo=open_tmp_file(file_name="./tmp.txt", mode="a+")  
write_tmp_file(fo, "test with file writing\n")
check_current_pos(fo)
close_tmp_file(fo)

fo=open_tmp_file(file_name="./tmp.txt", mode="r+")  
check_current_pos(fo)
r_buf = read_tmp_file(file_obj=fo, count=10)
print("READ_BUFF: ", r_buf)
check_current_pos(fo)
close_tmp_file(fo)


# OTHER EXAMPLES

# import os
# os.remove(file_name)
# os.rename(current_file_name, new_file_name)
# os.mkdir("newdir")
# os.chdir("newdir")
# os.getcwd()
# os.rmdir('dirname')


# PERMISSIONS

#  Modes   Description
#  r       Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
#  rb      Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
#  r+      Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
#  rb+     Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
#  w       Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#  wb      Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#  w+      Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file
#           for reading and writing.
#  wb+     Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a
#           newfile for reading and writing.
#  a       Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does
#           not exist, it creates a new file for writing.
#  ab      Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. 
#           If the file does not exist, it creates a new file for writing.
#  a+      Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
#           If the file does not exist, it creates a new file for reading and writing.
#  ab+     Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the 
#           append mode. If the file does not exist, it creates a new file for reading and writing.
