#Dylan and Avi
#4-25-18
#Haiku

import os

def create():
    haiku = []
    for i in range(3):
        line = raw_input("Enter haiku line number " + str(i+1) + ": ")
        line += "\n"
        haiku.append(line)
    name = raw_input("What do you want the name of the file to be (add .txt after name): ")
    f = open(name,"w+")
    for i in haiku:
        f.write(i)

def edit():
    name = raw_input("What is the name of the file you want to edit: ")
    line = input("What number is the line: ")
    f = open(name,"r")
    A = f.readlines()
    f.close()
    print A
    A[line-1] = raw_input("Enter the new line: ") + "\n"
    print A
    f = open(name,"w+")
    for i in A:
        f.write(i)

def main():
    valid = False
    while valid == False:
        choice = input("Do you want to make a haiku (1), edit a haiku (2), or end the program (3): ")
        if choice == 1:
            create()
        elif choice == 2:
            edit()
        elif choice == 3:
            valid = True
main()
