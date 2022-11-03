from math import *
def isfloat(num):
        try:
                float(num)
                return True
        except ValueError:
                return False
                
while True:
        base = input("Enter Base > ")
        if not isfloat(base):
                print("Enter a valid number")
                base = input("Enter Base > ")
        perpendicular = input("Enter Perpendicular > ")
        if not isfloat(perpendicular):
                print("Enter a valid number")
                perpendicular = input("Enter Perpendicular > ")
        sum1 = pow(float(base), 2) + pow(float(perpendicular), 2)
        result = sqrt(sum1)
        print("Hypotenuse is: " +str(result))
        print("Enter a number")
