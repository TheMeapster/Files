#Dylan and Avi
#4/25/18
#High Score

import os
from random import randint

def check(lis, num, player):
    for j in range(4,9):
        if num > j-4:
            print "Congratulations! Your score was high enough to get on the leaderboard."
            return str(num) + " " + player + "\n"
        else:
            print "You didn't get on the leaderboard."

def main():
    originals = [476, 92, 984, 5, 758, 320, 592, 603, 247, 818]
    A = open("high.txt", "r").read()
    lines = open("high.txt", "r").readlines()
    print "There is already a list of 5 highscores. Your score will be randomly generated and if it is high enough to be on the list it will be added."
    print "The highscores are \n", A
    A = A.split()
    for i in A:
        if i.isdigit():
            i = int(i)
        else:
            A.remove(i)
    name = raw_input("Enter your name (no spaces): ")
    score = randint(600,1000)
    lines[j-4] = check(lines, score, name)
    f = open("high.txt", "w")
    f.write("")
    f = open("high.txt", "a")
    for i in lines:
        f.write(str(i) + " " + name + "\n")
    print "The new highscores are" + open("high.txt", "r").read()
main()
