###############################################
# Name: Shweta Zutshi
# Class: CMPS 5363 Cryptography
# Date: 4 August 2015
# Program 3 - Ellipse Curve
###############################################
import math
import numpy as np
import matplotlib.pyplot as plt

#function to check and validate input points	
def checkInputs(x,y,a,b):
	if pow(y,2) == ( pow(x,3) + a*x + b):
	    return 0
	else:
	    return 1

#function to find the slope
def findSlope(x1,y1,x2,y2,a):
	m=0
	if x1 == x2 and y1 == y2:
		m = ((3*pow(x1,2))+a)/(2*y1)
	else:
		m = (y2-y1)/(x2-x1)
	return m 
 
#function to find the third point 
def findThirdPoint(m,x1,y1,x2):
	x3 = 0
	y3 =0
    
	x3 = pow(m,2)-x1-x2
	y3 = m*(x3-x1)+y1
	return x3,y3

#function to plot the curve
def plotCurve(w,h,x1,y1,x2,y2,m,x3,y3,a,b):
	#annotate the plot
    an1 = plt.annotate("Shweta Zutshi", xy=(-w+2 , h-2), xycoords="data",va="center", ha="center",bbox=dict(boxstyle="round", fc="w"))
	#creating a mesh grid
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
	#plotting the curve
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])
	#plotting point1
    plt.plot(x1, y1,'ro')
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)
	#plotting point2
    plt.plot(x2, y2,'ro')
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)
	#plotting line passing through points
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))
	#plotting point3
    plt.plot(x3, y3,'yo')
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)
    plt.grid()
    plt.show()
	


