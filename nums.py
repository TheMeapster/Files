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
    print "The average of numsText.txt is: ", A[len(A)/2]
    count = 0
    finalCount = 0
    mostCommon = 0
    for i in range(1,len(A)):
        if A[i] == A[i-1]:
            count += 1
        else:
            if count > finalCount:
                finalCount = count
                mostCommon = A[i]
            count = 1
    print A
    print "The most common number in numsText.txt: ", mostCommon, "and this number repeats", finalCount, "times"
main()
