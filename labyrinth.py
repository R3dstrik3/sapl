#!/usr/bin/env python3

#This python script searches the shortest way, through a given labyrinth.

import sys
import os.path

class Point:
      def __init__(self, x, y):
            self.x = x
            self.y = y

position = Point(0,0)

def getsteps():
      return (1, 2, 3)

def rekursion(last_step):
      for step in getsteps():
            print(step)
            
if len(sys.argv) < 2:
      print("Not enought arguments.")
      sys.exit(2)
elif not os.path.isfile(sys.argv[1]):
      print("The given argument is not a file.")
      sys.exit(2)

width = -1
height = 0
with open (sys.argv[1]) as f:
      for line in f:
            try:
                  position = Point(line.rindex("E"), height+1)
            except ValueError:
                  print("nope not in this line")
            height = height + 1
            if width == -1:
                  width = len(line)
            elif len(line) != width:
                  print("Nicht quadratisch!")
                  sys.exit(1)

width = width - 1
print("width =",width)
print("height =",height)
print(position.x,position.y)
rekursion(0)

Matrix = [[0 for x in range(width)] for x in range(height)]
with open (sys.argv[1]) as f:
      for line in f:
            
