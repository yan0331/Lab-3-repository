#!/usr/bin/env python3

def write_a_text_file():
    my_name = input("Enter your name: ")
    file_name = my_name + ".txt"
    file = open(file_name, "w")
    file.write(my_name)
    file.close()

write_a_text_file()
