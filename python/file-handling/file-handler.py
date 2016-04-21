#!/usr/bin/python

def create_update_file(file_name) :
    fo=open(file_name, "w+")
    fo.write("This is line number 1\n");
    fo.close()
    return

def main():
    create_update_file("tmp.txt");
    return

main()
