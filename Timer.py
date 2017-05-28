from threading import Timer
import time
import pyglet

class Timer:

    def welcome(self):
        print("Welcome to the Choco timer. Please type 'feeddachocos' to begin")

    def ding(self):
        music = pyglet.resource.media('chocoboThemeClip.mp3')
        music.play()
        pyglet.app.run()

    def startTimer(self, timeLength):
        t = Timer(timeLength, self.ding)
        t.start()

