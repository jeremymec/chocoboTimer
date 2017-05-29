from Timer import *

if __name__ == "__main__":
    t = Timer()
    t.welcome()
    while True:
        usrInp = input("> ")
        if usrInp == "fed":
            t.startTimer(2)
            print("Time started")




