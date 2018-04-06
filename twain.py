#Files/Twain
#Dylan and Avi

def main():
    f=open("twain.txt","r")
    B = f.readlines()
    f.close()
    for i in B:
        for j in i:
            B.append(j)
        B.remove(i)
    vowels = ["a","e","i","o","u"]
    vowelCount = 0
    consonants = 0
    for i in B:
        if i in vowels:
            vowelCount += 1
    print "The amount of vowels is:", vowelCount
    nut = [".","?",",","!",";",":"]
    for i in nut:
        print i, "appears", B.count(i), "times."
    letts = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    f=open("avoid.txt","r")
    C = f.readlines()
    f.close()
    for i in C:
        for j in i:
            C.append(j)
        C.remove(i)
    for i in letts:
        print i, "appears", C.count(i), "times."
main()
