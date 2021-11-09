#this is a script to generate probe points using parametric equation of circle 
import math

f = open("datapoints.txt", "a")
delta_l = 0.000001
r = 0.05 + delta_l
for theta in range(0,3600,1):
	theta = theta*0.1
	theta = math.radians(theta)
	x = -1*r*math.cos(theta)
	y = r*math.sin(theta)
	s = "( " + str(x) + " " + str(y) + "  0 ) // theta value " + str(theta) + "\n"
	f.write(s)

f.close()  
