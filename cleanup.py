#used to clean up your dictionary to pertain to what you need for letters
#deleting all upper case words and letters that dont start with those in greek alphabet

import fileinput
def parseText(yourfile):
    for line in fileinput.input(yourfile, inplace=True):
        if line[0]=='A':
            continue
        if line[0]=='B':
            continue
        if line[0]=='C':
                continue
        if line[0]=='D':
            continue
        if line[0]=='E':
            continue
        if line[0]=='F':
            continue
        if line[0]=='G':
            continue
        if line[0]=='H':
            continue
        if line[0]=='I':
            continue
        if line[0]=='J':
            continue
        if line[0]=='K':
            continue
        if line[0]=='L':
            continue
        if line[0]=='M':
            continue
        if line[0]=='N':
            continue
        if line[0]=='O':
            continue
        if line[0]=='P':
            continue
        if line[0]=='Q':
            continue
        if line[0]=='R':
            continue
        if line[0]=='S':
            continue
        if line[0]=='T':
            continue
        if line[0]=='U':
            continue
        if line[0]=='V':
            continue
        if line[0]=='W':
            continue
        if line[0]=='X':
            continue
        if line[0]=='Y':
            continue
        if line[0]=='Z':
            continue
        if line[0]=='h':
            continue
        if line[0]=='j':
            continue
        if line[0]=='q':
            continue
        if line[0]=='v':
            continue
        if line[0]=='w':
            continue
        if line[0]=='y':
            continue
        print line,

if __name__ == '__main__':
    parseText('words2.txt')