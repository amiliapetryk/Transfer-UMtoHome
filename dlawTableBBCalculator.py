# the goal of this script is to take a starting shock radius and density plateau and output the values necessary for a dlaw table that creates an r2 density profile before levelling off

# import packages
import math

finalDen = 2.0	
finalDen = 1.5291512060576232e-05
distance = 2500	
end = 20	

angularDiameterDeg = 0.65764 	# degrees
angularDiameterRad = angularDiameterDeg*(math.pi/180) 	# rad
radius = distance*math.tan(angularDiameterRad)/2	# pc
radiusCm = radius * (3.086e18) 				# cm

#print("Distance of {} corresponds to radius of {}.".format(distance,radius))

# there are initial, middle, and final distances
initialDistance = 10 * (1.496e13) # AU * (cm/AU) = cm
middleDistance = -9999
finalDistance = -9999

# there will be initial and final densities
initialDensity = -9999
finalDensity = -9999

# for equation of the form y = ax^2 + bx + c (where c=0), for a given radius (x) and density (y) we can solve for a and b
# rho = Mdot / (4*pi*r^2*v)
# form of y = k/x^2, k = Mdot/(4*pi*v) where y is rho and x is r
k = finalDen * (radiusCm**2) # H/cm^3 * cm^2 = H/cm
#a = (2*finalDen)/(2*(radius**2))
#b = abs((finalDen-(a*(radius**2)))/radius)
#c = a*(initialDistance**2) + b*(initialDistance)

# find initialDensity that corresponds with initialDistance
initialDensity = k / (initialDistance**2)
initialDensity = 1339558.9303406526
print("initial density is {}".format(initialDensity))

# at the shock front
middleDistance = radius
finalDensity = finalDen
finalDensity = 1.5291512060576232e-05

# convert all values to log for table
logInitialDist = math.log10(initialDistance)
logInitialDen = math.log10(initialDensity)

logMiddleDist = math.log10(radiusCm)

logFinalDist = end
logFinalDen = math.log10(finalDensity)

# print dlaw table to input in table.in files
print("\ndlaw table\ncontinue {} {}\ncontinue {} {}\ncontinue {} {}\nend of dlaw".format(logInitialDist,logInitialDen,logMiddleDist,logFinalDen,logFinalDist,logFinalDen))
