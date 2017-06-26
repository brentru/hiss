# hiss: menubar app for finding Adafruit CircuitPython boards
# brent rubell, 2017 (github.com/brentru)
import subprocess, os
import sys, argparse
from os import system
from rumps import *

class hiss(rumps.App):
    def __init__(self):
        super(hiss, self).__init__("hiss")
        self.menu = ["Locate"]
        quit_button = 'Quit'
        rumps.debug_mode(False) # dbg

    @rumps.clicked("Locate")
    def locate(self, _):
     p = subprocess.Popen('ls /dev/cu.usbmodem*', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
     for line in p.stdout.readlines():
         print " ",
     retval = p.wait()
     err = line[:2]
     if err == 'ls':
        rumps.alert("No Board Found (Check your USB Connection and try again..)")
     else: 
       #print line + " copied to local clipboard"
       os.system("echo '%s' | pbcopy" % line)
       rumps.alert("Board Found: ", line)


if __name__ == "__main__":
    hiss().run()