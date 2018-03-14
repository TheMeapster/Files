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
    divs31 = []
    for i in A:
        if A.count(i) > count:
            count = A.count(i)
            mostCommon = i
        if i%31 == 0:
            divs31.append(i)
    divs31 = list(set(divs31))
    divs31.sort()
    print "The most common number in numsText.txt", mostCommon, "and this number repeats", count, "times."
    print "The numbers that are divisible by 31 are", divs31
main()
