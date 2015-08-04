###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 4 August 2015
# Program 3 - Ellipse Curve
###############################################
import argparse
import sys
from fractions import Fraction
import ellipse as e

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="x coordinate of point1")
    parser.add_argument("-y1",dest="y1", help="y coordinate of point1")
    parser.add_argument("-x2",dest="x2", help="x coordinate of point2")
    parser.add_argument("-y2",dest="y2", help="y coordinate of point2")

    args = parser.parse_args()

    a = Fraction(args.a)
    b = Fraction(args.b)
    x1 = Fraction(args.x1)
    y1 = Fraction(args.y1)
    x2 = Fraction(args.x2)
    y2 = Fraction(args.y2)
    m =0
    x3 =0
    y3 =0
    print(a,b,x1,y1,x2,y2)
	#validating the inputs
    if e.checkInputs(x1,y1,a,b) == 0 and e.checkInputs(x2,y2,a,b) == 0:
        print("Both the points are on the curve")
        #finding the slope
        m = e.findSlope(x1,y1,x2,y2,a)
        print("The slope is: ",m)
        #finding the third point
        x3,y3 = e.findThirdPoint(m,x1,y1,x2)
        print("The third point is: ",x3,y3)
        #finding the maximum out of all values
        maxValue = max(abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3))
        #width and height of the plot
        w = maxValue+10
        h = maxValue +10
        #plotting the curve
        e.plotCurve(w,h,x1,y1,x2,y2,m,x3,y3,a,b)
    else:
        print("One or both the points are not on the curve")
        

if __name__ == '__main__':
    main()