#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 03.05.2017
# Purpose : Classes in Python

class Car():
	def __init__(self):
		print "Car started"
	def color(self,color)
		print "Your %s car is looking awesome" % color
	def accel(self,speed):
		print "Speeding upto %s mph" % speed
	def turn(self,direction):
		print "Turning " + direction
	def stop(self):
		print "Stop"
car1 = Car()
print car1
print car1.color('Black Chevrolet Cobalt SS')
print car1.accel(50)
print car1.turn('Right')
print car1.stop()


# END
