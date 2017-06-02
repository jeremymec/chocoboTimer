from threading import Timer as PyTimer
import time
import pyglet


class Timer(object):

    timerList = []
    x = 0

    def welcome(self):
        print("Welcome to the Choco timer. Please type 'fed' to begin")

    def printList(self):
        for timer in self.timerList:
            started = timer[1]
            deltaT = time.time() - started
            remain = timer[2] - deltaT
            print("Time " + str(self.x) + " is running, and has " + self.processTime(remain) + " remaining")

    def processTime(self, t):
        minutes, seconds = divmod(t, 60)
        minutes = int(minutes)
        seconds = int(seconds)
        return str(minutes) + " minutes and " + str(seconds) + " seconds"

    def updateList(self):
        for timer in self.timerList:
            started = timer[1]
            deltaT = time.time() - started
            remain = timer[2] - deltaT
            if remain < 0:
                self.timerList.remove(timer)

    def ding(self):
        print("ding")
        music = pyglet.resource.media('chocoThemeClip.wav')
        music.play()
        pyglet.app.run()
        self.updateList()

    def startTimer(self, timeLength):
        self.x += 1
        t = PyTimer(timeLength, self.ding)
        t.start()
        self.timerList.append([t, time.time(), timeLength])

