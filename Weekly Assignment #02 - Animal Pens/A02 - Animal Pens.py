# Author:Marcais Jackson
#This program uses mathematical assignments to solve a geometry problem.

#from math import pi, is the mathematical constant 3.141592, to available precision.
from math import pi
#Functions
def FindArea(height,length):
   return height*length
def FindAreaForRadius(radius):
   return pi*radius*radius
def FindPerimeter(height,length):
   return 2*(height+length)
def FindPerimeterForRadius(radius):
   return 2*pi*radius
#Prompting user to enter height, length for cow, rhino, turtle and bird radius.
cow_length = input("Please enter a value for cow-length: ")
cow_height = input("Please enter a value for cow-height: ")
rhino_length = input("Please enter a value for rhino-length: ")
rhino_height = input("Please enter a value for rhino-height: ")
turtle_length = input("Please enter a value for turtle-length: ")
turtle_height = input("Please enter a value for turtle-height : ")

bird_radius = input("Please enter a value for bird-radius: ")

#Calling functions to calculate areas
cow_area = FindArea(cow_height,cow_length)
rhino_area = FindArea(rhino_height,rhino_length)
turtle_area = FindArea(turtle_height,turtle_length)
bird_area = FindAreaForRadius(bird_radius)
total_area = cow_area + rhino_area + turtle_area + bird_area
#Calling functions to calculate perimeter
cow_perimeter = FindPerimeter(cow_height,cow_length)
rhino_perimeter = FindPerimeter(rhino_height,rhino_length)
turtle_perimeter = FindPerimeter(turtle_height,turtle_length)
bird_perimeter = FindPerimeterForRadius(bird_radius)
total_perimeter = cow_perimeter + rhino_perimeter + turtle_perimeter + bird_perimeter


#Printing all of the areas and perimeters for cow, bird, turtle and rhino.
print "The area of the \"Moo Cow Pen\" is : ", cow_area
print "The perimeter of the \"Moo Cow Pen\" is: ", cow_perimeter
print "The area of the \"Rhino Common ground\" is: ", rhino_area
print "The perimeter of the \"Rhino Common ground\" is: ", rhino_perimeter
print "The area of the \"Turtle Petting Area\" is: ", turtle_area
print "The perimeter of the \"Turtle Petting Area\" is: ", turtle_perimeter
print "The area of the \"Bird Cage\" is: ", bird_area
print "The perimeter of the \"Bird Cage\" is: ", bird_perimeter
#I added this line to help make stuff easier to read.
print "___________________________________________________________________"
print ""
#Printing the total perimeter and area.
print "The TOTAL AREA of all regions is: ", total_area
print "The TOTAL LENGTH of all fences is: ",total_perimeter
#End program.
raw_input("Press Any Key To Continue")
