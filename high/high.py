#Dylan and Avi
#4/25/18
#High Score

import os
import time
from random import randint

def main():
    os.system("clear")
    A = open("high.txt", "r").read()
    print "There is already a list of 5 highscores. Your score will be randomly generated and if it is high enough to be on the list it will be added. \n"
    print "The highscores are: \n", A
    A = A.split()
    B = open("high.txt", "r").readlines()
    for i in A:
        if i.isdigit():
            i = int(i)
        else:
            A.remove(i)
    count = 0
    for i in A:
        A[count] = int(i)
        count += 1
    name = raw_input("Enter your name (spaces will be changed to underscores): ")
    finalName = ""
    for i in name:
        if i == " ":
            i = "_"
        finalName += i
    score = 895
    os.system("clear")
    index = 0
    valid = True
    for j in range(10):
        if valid:
            if score >= A[index]:
                B.pop(9)
                B.insert(index, str(score) + " " + finalName + "\n")
                print "Your score of", score, "placed number", j + 1, "on the table. \n"
                valid = False
            elif j == 9:
                print "Your score of", score, "was not high enough to get on the table. \n"
                valid == False
            else:
                index += 1
    f = open("high.txt", "w")
    for i in B:
        f.write(str(i))
    f.close()
    C = open("high.txt", "r").read()
    print "The new highscores are: \n", C
    time.sleep(3)
main()
