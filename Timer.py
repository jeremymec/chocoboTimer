from threading import Timer as PyTimer
import time
import pyglet


class Timer(object):

    def welcome(self):
        print("Welcome to the Choco timer. Please type 'fed' to begin")

    def ding(self):
        print("ding")
        music = pyglet.resource.media('chocoThemeClip.wav')
        music.play()
        pyglet.app.run()

    def startTimer(self, timeLength):
        t = PyTimer(timeLength, self.ding)
        t.start()

