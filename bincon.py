#
#
#
#
#


# PYTHON BINARY INTERPRETER
import sys

def make_string(binary, bitLength):
    sent = []

    while True:
        ch = chr(int(binary[:bitLength], 2))

        if(ch == '\b'):
            sent = sent[:-1]

        else:
            sent.append(ch)

        if(len(binary) > bitLength):
            binary = binary[bitLength:]

        else:
            break

    print
    for char in sent:
        sys.stdout.write(char)
    print


def clean(string):
    string = string.replace(' ', '')
    string = string.replace('\n', '')
    return string



bi = sys.stdin.read()
bi = clean(bi)

if(bi == ""):
    print("No Input Recieved")
    exit()

biLen = len(bi)
if(biLen % 8 == 0 and biLen % 7 == 0):
    make_string(bi, 7)
    make_string(bi, 8)

elif(biLen % 7 == 0):
    make_string(bi, 7)

elif(biLen % 8 == 0):
    make_string(bi, 8)

else:
    print("Not comprised of only 7 bits or only 8 bits.")
    exit()
