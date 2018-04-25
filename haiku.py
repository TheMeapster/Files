#Dylan and Avi
#4-25-18
#Haiku

import os

files = []

def create():
    haiku = []
    for i in range(3):
        line = raw_input("Enter haiku line number " + str(i+1) + ": ")
        line += "\n"
        haiku.append(line)
    name = raw_input("What do you want the haiku of the file to be: ") + ".txt"
    files.append(name)
    f = open(name,"w+")
    for i in haiku:
        f.write(i)

def edit():
    name = raw_input("What is the name of the haiku you want to edit: ") + ".txt"
    line = input("What number is the line: ")
    A = open(name,"r").readlines()
    A[line-1] = raw_input("Enter the new line: ") + "\n"
    f = open(name,"w+")
    for i in A:
        f.write(i)

def view():
    name = raw_input("What is the name of the haiku you want to read: ") + ".txt"
    print open(name, "r").read()
def main():
    valid = True
    while valid:
        choice = input("Do you want to make a haiku (1), edit a haiku (2), read a haiku (3), or end the program (4): ")
        if choice == 1:
            create()
        elif choice == 2:
            edit()
        elif choice == 3:
            view()
        elif choice == 4:
            for i in files:
                os.remove(i)
            valid = False


main()
