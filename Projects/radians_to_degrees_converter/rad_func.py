from math import pi
def radToDegree_converter():
    angle_in_radians = int(input("Enter an angle in radians: "))
    angle_in_degrees = round(angle_in_radians*180/pi)
    print(str(angle_in_radians) + " radians is " + str(angle_in_degrees) + " degrees to the nearest whole number.")
    return(angle_in_degrees)
radToDegree_converter()