#Files/nums
#Dylan and Avi
#2/28/18
from os import *

def main():
    x = "numsText.txt"
    f = open(x, "r")
    A = f.readlines()
    f.close()
    print A
main()
