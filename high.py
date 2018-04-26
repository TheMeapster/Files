#Dylan and Avi
#4/25/18
#High Score

import os
from random import randint

def main():
    A = open("high.txt", "r").read()
    print "There is already a list of 5 highscores. Your score will be randomly generated and if it is high enough to be on the list it will be added."
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
    name = raw_input("Enter your name (no spaces): ")
    score = 997
    index = 0
    valid = True
    for j in range(6):
        if valid:
            if score > A[index]:
                B.pop(4)
                B.insert(index, str(score) + " " + name + "\n")
                print B
                valid = False
            else:
                index += 1
    f = open("high.txt", "w")
    for i in B:
        f.write(str(i))
    print "The new highscores are" + open("high.txt", "r").read()
main()
