#Files/Dick
#Dylan and Avi
#3/15/18

import os

def main():
    f=open("dick.txt","r")
    A = f.readlines()
    f.close()
    fives = []
    for i in A:
        if len(i) == 6:
            fives.append(i)
    print "The number of five letter words is:", len(fives)
    threeS = []
    for i in A:
        sCount = 0
        for j in i:
            if j == 's':
                sCount += 1
        if sCount == 3:
            threeS.append(i)
    print "The number of words with three s's is:", len(threeS)
    startF = []
    for i in A:
        if i[0] == 'f':
            startF.append(i)
    print "The number of words that start with F is:", len(startF)
main()
