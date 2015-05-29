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
      return (Point(1,0), Point(0,1), Point(-1,0), Point(0,-1))

def rekursion(last_step, position):
      print position
      for line in Matrix:
            print(line)
      for step in getsteps():
            if last_step.x != step.x | last_step.y != step.y:
                  try:
                        if Matrix[position.x+step.x][position.y+step.y] == ' ':
                              Matrix[position.x+step.x][position.y+step.y] = 'E'
                              Matrix[position.x][position.y] = ' '
                              position = Point(position.x+step.x, position.y+step.y)
                              if rekursion(Point(-step.x,-step.y), position) == 1:
                                    return 1
                              Matrix[position.x][position.y] = ' '
                              position = Point(position.x-step.x, position.y-step.y)
                              Matrix[position.x][position.y] = 'E'
                        elif Matrix[position.x+step.x][position.y+step.y] == 'A':
                              return 1
                  except IndexError:
                        print()
      return 0
            
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
                  position = Point(height, line.rindex("E"))
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

Matrix = [[0 for x in range(width+1)] for x in range(height)]
x = -1
y = 0
with open (sys.argv[1]) as f:
      for line in f:
            x = x + 1
            y = 0
            for char in line:
                  Matrix[x][y] = char
                  y = y + 1


print rekursion(Point(0,0), position)
