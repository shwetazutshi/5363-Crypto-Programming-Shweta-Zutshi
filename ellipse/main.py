###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 3 August 2015
# Program 3 - Ellipse Curve
###############################################
import argparse
import sys
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

    a = int(args.a)
    b = int(args.b)
    x1 = int(args.x1)
    y1 = int(args.y1)
    x2 = int(args.x2)
    y2 = int(args.y2)
    m =0
    x3 =0
    y3 =0
    print(a,b,x1,y1,x2,y2)
    e.checkInputs(x1,y1,a,b)
    e.checkInputs(x2,y2,a,b)
    m = e.findSlope(x1,y1,x2,y2,a)
    print(m)
    x3,y3 = e.findThirdPoint(m,x1,y1,x2)
    print(x3,y3)
    max1 = max(abs(x1),abs(y1),abs(x2),abs(y2),abs(x3),abs(y3))
    
    w = max1 + 10
    h = max1 + 10
    e.plotCurve(w,h,x1,y1,x2,y2,m,x3,y3)

if __name__ == '__main__':
    main()