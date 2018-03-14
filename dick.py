#Files/Dick
#Dylan and Avi
#3/15/18

import os

def main():
    f=open("dick.txt","r")
    A = f.readlines()
    f.close()
    fiveCount = []
    for i in A:
        if len(i) == 5:
            fiveCount.append(i)
    print "The number of five letter words is:", len(fiveCount)
main()
