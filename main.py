from Timer import *

if __name__ == "__main__":
    t = Timer()
    t.welcome()
    while True:
        usrInp = input("> ")
        if usrInp == "fed":
            t.startTimer(3600)
            print("Time started")
        elif usrInp == "status":
            t.printList()
        else:
            print("Did not understand command")


