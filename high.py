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
    print "B", B
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
    score = randint(1,1000)
    os.system("clear")
    print score
    index = 0
    valid = True
    for j in range(11):
        if valid:
            print A[index], score
            if score > A[index]:
                B.pop(9)
                print A[index], score
                B.insert(index, str(score) + "\t" + name + "\n")
                print "Your score of", score, "placed number", j + 1, "on the table. \n"
                valid = False
            elif j == 10:
                print "Your score of", score, "was not high enough to get on the table. \n"
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
