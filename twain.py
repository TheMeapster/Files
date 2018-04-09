#Files/Twain
#Dylan and Avi

def readlines(fileName):
    f=open(fileName,"r")
    A = f.readlines()
    f.close()
    for i in A:
        for j in i:
            A.append(j)
        A.remove(i)
    return A

def main():
    B = readlines("shorttwain.txt")
    C = readlines("twain.txt")
    D = readlines("avoid.txt")
    vowels = ["a","e","i","o","u"]
    vowelCount = 0
    for i in B:
        if i in vowels:
            vowelCount += 1
    print "The amount of vowels in shorttwain.txt is:", vowelCount
    letts = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in letts:
        print i, "appears in avoid.txt", D.count(i), "times."
    nut = [".","?",",","!",";",":"]
    for i in nut:
        print i, "appears in shorttwain.txt", B.count(i), "times."
    for i in nut:
        print i, "appears in twain.txt", C.count(i), "times."
main()
