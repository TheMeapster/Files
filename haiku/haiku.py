#Dylan and Avi
#4-25-18
#Haiku

import os
import time

def create(filez):
    os.system("clear")
    haiku = []
    for i in range(3):
        line = raw_input("Enter haiku line number " + str(i+1) + ": ")
        line += "\n"
        haiku.append(line)
    valid = True
    while valid:
        name = raw_input("What do you want the haiku of the file to be: ") + ".txt"
        if name in filez:
            choice = input("That file name is already being used. Do you want to overwrite the current file (1) or change the file name (2): ")
            if choice == 1:
                valid = False
        else:
            valid = False
    filez.append(name)
    f = open("./txt/" + name,"w+")
    for i in haiku:
        f.write(i)
    return filez

def edit(filez):
    os.system("clear")
    valid = True
    while valid:
        name = raw_input("What is the name of the haiku you want to edit: ") + ".txt"
        line = input("What number is the line: ")
        if name in filez:
            A = open("./txt/" + name,"r").readlines()
            A[line-1] = raw_input("Enter the new line: ") + "\n"
            f = open("./txt/" + name,"w+")
            for i in A:
                f.write(i)
            valid = False
        else:
            print "That is not a valid file name."
    return filez

# def view():
#     name = raw_input("What is the name of the haiku you want to read: ") + ".txt"
#     print open(name,"r").read

def view(filez):
    os.system("clear")
    valid = True
    while valid:
        name = raw_input("What is the name of the haiku you want to read: ") + ".txt"
        if name in filez:
            with open("./txt/" + name) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            os.system("clear")
            for line in content:
                print(line)
                time.sleep(1)
            time.sleep(2)
            valid = False
        else:
            print "That is not a valid file name."
    return filez

def delete(filez):
    os.system("clear")
    valid = True
    while valid:
        name = raw_input("What is the name of the haiku you want to read: ") + ".txt"
        if name in filez:
            os.remove("./txt/" + name)
            print name, "has been deleted."
        else:
            print "That is not a valid file name."
    return filez

def main():
    os.system("clear")
    valid = True
    while valid:
        files = os.listdir("./txt")
        os.system("clear")
        choice = input("Do you want to make a haiku (1), edit a haiku (2), read a haiku (3), delete a haiku (4), or end the program (5): ")
        if choice == 1:
            files = create(files)
        elif choice == 2:
            files = edit(files)
        elif choice == 3:
            files = view(files)
        elif choice == 4:
            files = delete(files)
        elif choice == 5:
            valid = False

main()
