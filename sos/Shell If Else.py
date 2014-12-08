#SOS
import RPi.GPIO as GP,time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#Defining dot
def dot():
    GP.output(11, True)
    time.sleep(0.5)
    GP.output(11, False)
    time.sleep(0.5)
dot()

#Defining dash
def dash():
    GP.output(11, True)
    time.sleep(2)
    GP.output(11, False)
    time.sleep(0.5)
dash()
#Defining morse
def morse(name):
    if name == "A":
        dot()
        dash()
        print("A")
    elif name == "B":
        dash()
        dot()
        dot()
        dot()
        print("B")
    elif name == "C":
        dash()
        dot()
        dash()
        dot()
        print("C")
    elif name == "D":
        dash()
        dot()
        dot()
        print("D")
    elif name == "E":
        dot()
        print("E")
    elif name == "F":
        dot()
        dot()
        dash()
        dot()
        print("F")
    elif name == "G":
        dash()
        dash()
        dot()
        print("G")
    elif name == "H":
        dot()
        dot()
        dot()
        dot()
        print("H")
    elif name == "I":
        dot()
        dot()
        print("I")
    elif name == "J":
        dot()
        dash()
        dash()
        dash()
        print("J")
    elif name == "K":
        dash()
        dot()
        dash()
        print("K")
    elif name == "L":
        dot()
        dash()
        dot()
        dot()
        print("L")
    elif name == "M":
        dash()
        dash()
        print("M")
    elif name == "N":
        dash()
        dot()
        print("N")
    elif name == "O":
        dash()
        dash()
        dash()
        print("O")
    elif name == "P":
        dot()
        dash()
        dash()
        dot()
        print("P")
    elif name == "Q":
        dash()
        dash()
        dot()
        dash()
        print("Q")
    elif name == "R":
        dot()
        dash()
        dot()
        print("R")
    elif name == "S":
        dot()
        dot()
        dot()
        print("S")
    elif name == "T":
        dash()
        print("T")
    elif name == "U":
        dot()
        dot()
        dash()
        print("U")
    elif name == "V":
        dot()
        dot()
        dot()
        dash()
        print("V")
    elif name == "W":
        dot()
        dash()
        dash()
        print("W")
    elif name == "X":
        dash()
        dot()
        dot()
        dash()
        print("X")
    elif name == "Y":
        dash()
        dot()
        dash()
        dash()
        print("Y")
    elif name == "Z":
        dash()
        dash()
        dot()
        dot()
        print ("Z")
    elif name == " ":
        time.sleep(3)
        print(" ")

msg=input("What do you want me to say IN CAPITALS?")
for each in msg:
    morse(each)
