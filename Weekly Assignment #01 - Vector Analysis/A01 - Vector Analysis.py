# Author:Marcais Jackson
#This program calculates the sum, difference, and magnitudes of two user defined vectors.

#import math provides access to mathematical functions.
import math

#Initializing and taking inputs.
name=raw_input("Please enter your name: ")

x1 = float(input("Please enter the X coordinate of first vector: "));
y1 = float(input("Please enter the Y coordinate of first vector: "));

x2 = float(input("Please enter the X coordinate of second vector: "));
y2 = float(input("Please enter the Y coordinate of second vector: "));

#Calculating magnitude of vectors.
mag1=math.sqrt(x1*x1 + y1*y1);
mag2=math.sqrt(x2*x2 + y2*y2);

#Calculating sum of vectors.
sum_x = x1+x2;
sum_y = y1+y2;

#Calculating difference of vectors.
diff_x = x1-x2;
diff_y = y1-y2;

#Printing the name of the user, magnitude, sum and difference of the two vectors.
print("The name of the user is: ",name);
print("The magnitude of first vector is: ", round(mag1,3));
print("The magnitude of second vector is: ", round(mag2,3));
print("The sum of the two vectors is: (", round(sum_x,3),",",round(sum_y,3),")");
print("The difference of the two vectors is: (", round(diff_x,3),",",round(diff_y,3),")");
#End program.
raw_input("Press Any Key To Continue")