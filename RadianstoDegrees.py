# Creating a function that takes an angle in radians and returns the corresponding angle in degrees
# The result is rounded to one decimal place
# The basis comes from the formular rad * 180/pi = degrees
# Hence, there is need in applying the math module
# The format tool is used to ensure that the printed result is in 2 decimal places
from math import pi
radianValue = input("Enter the Radians you wish to convert : ")
print("You have entered ", radianValue)
radiansToDegrees = float (radianValue) * (180/pi)
print("Converting " + radianValue + " Rads gives: ""{:.02f}".format(radiansToDegrees),"\N{degree sign}")