# the goal of this script is to take a starting shock radius and density plateau and output the values necessary for a dlaw table that creates an r2 density profile before levelling off

# import packages
import math

finalDen = 2.0			# other options are 2.0, 5.0
distance = 2500			# other options are 2500, 2800
end = 20			# some point beyong 19.695 (the largest possible radius)

angularDiameterDeg = 0.65764 	# degrees
angularDiameterRad = angularDiameterDeg*(math.pi/180) 	# rad
radius = distance*math.tan(angularDiameterRad)/2	# pc

#print("Distance of {} corresponds to radius of {}.".format(distance,radius))

# there will be initial, middle, and final distances
initialDistance = -9999
middleDistance = -9999
finalDistance = -9999

# there will be initial and final densities
initialDensity = -9999
finalDensity = -9999

# for equation of the form y = ax^2 + bx + c (where c=0), for a given radius (x) and density (y) we can solve for a and b
a = (2*finalDen)/(2*(radius**2))
b = abs((finalDen-(a*(radius**2)))/radius)
c = 0 

# pick a point very close to (0,0)
initialDistance = 1e-13
initialDensity = a*(initialDistance**2) + b*initialDistance + c

# at the shock front
middleDistance = radius
finalDensity = finalDen

# convert all values to log for table
logInitialDist = math.log10(initialDistance*(3.086e18))
logInitialDen = math.log10(initialDensity)

logMiddleDist = math.log10(radius*(3.086e18))

logFinalDist = end
logFinalDen = math.log10(finalDensity)

# print dlaw table to input in table.in files
print("\ndlaw table\ncontinue {} {}\ncontinue {} {}\ncontinue {} {}\nend of dlaw".format(logInitialDist,logInitialDen,logMiddleDist,logFinalDen,logFinalDist,logFinalDen))
