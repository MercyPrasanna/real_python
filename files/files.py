# Writing a file, \n will create a new line.
with open("test.txt", "w") as write_file:
    lines = ["first line.\n", "second line.\n", "third line.\n"]
    write_file.writelines(lines)

# Reading a file
with open("test.txt", "r") as read_file:
    lines = read_file.readlines()
    for line in lines:
        print(line)

import glob
import os

""" Loops through all the files, checks if its a file and then check if its a
    csv and then print the absolute path."""
for filep in glob.glob("**/*", recursive=True):
    if os.path.isfile(filep):
        if os.path.splitext(filep)[1] == ".csv":
            print(os.path.join(os.getcwd(), filep))
