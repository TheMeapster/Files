#Dylan and Avi
#4/25/18
#Top Ten

import os
from random import randint

def main():
    originals = [476, 92, 984, 5, 758, 320, 592, 603, 247, 818]
    A = open("top.txt", "r").read()
    print "There is already a list of 10 numbers and 10 more numbers will be randomly generated and if they are not in the current list they will be added."
    print "The original list is: \n", A
    for i in range(10):
        num = 5
        if str(num) + "\n" in A:
            print num, "is already in the list."
        else:
            print num, "is not in the list and will be added."
            f = open("top.txt","a")
            f.write(str(num) + "\n")
            f.close()
    print "The final list is: \n", open("top.txt", "r").read()
    f = open("top.txt", "w")
    f.write("")
    f = open("top.txt", "a")
    for i in originals:
        f.write(str(i) + "\n")
main()
