#Files/nums
#Dylan and Avi
#2/28/18
import os

def main():
    f=open("numsText.txt","r")
    A = f.readlines()
    f.close()
    for i in range(len(A)):
        A[i] = int(A[i])
    A.sort()
    count = 0
    mostCommon = 0
    for i in range(1,len(A)):
        if i.count(A):
            count = i.count(A)
            mostCommon = i
    print A
    print "The most common number in numsText.txt: ", mostCommon, "and this number repeats", finalCount, "times"
main()
