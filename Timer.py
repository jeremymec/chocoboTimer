from threading import Timer
import time

class Timer:

    def welcome(self):
        print("Welcome to the Choco timer. Please type 'feeddachocos' to begin")

    def ding(self):
        print("ding")

    def startTimer(self, timeLength):
        t = Timer(timeLength, self.ding)
        t.start()

