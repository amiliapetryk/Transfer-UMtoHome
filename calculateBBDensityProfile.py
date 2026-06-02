# the goal of this script is to calculate and plot the density profile for different parameter inputs (stellar wind model)
# equation of stellar structure: Mdot = 4*pi*r^2*rho*v -> rho = Mdot/(4*pi*r^2*v) 

import math
import numpy as np
import matplotlib.pyplot as plt

# parameters for blackbody
vel = 1000 * (100000/1) # km/s * (100000 cm/1 km) = cm/s
mdot1 = 1e-6 * (1.989e33/1) * (1/31557600) # solar mass/year * (1.989e33 g/solar mass) * (1 year/31557600 seconds) = g/s
mdot2 = 1e-7 * (1.989e33/1) * (1/31557600) # solar mass/year * (1.989e33 g/solar mass) * (1 year/31557600 seconds) = g/s
ri = 10 * (1.496e13/1) # AU * (1.496e13 cm/AU) = cm
rf = 14.348 * (3.086e18/1) # pc * (3.086e18 cm/pc) = cm -> equivalent to distance of 2500 pc
hden = 2.0 # atoms/cm^3
num = 1000



# create radius and density arrays
radArray = np.logspace(math.log10(ri),math.log10(rf),num)
den1Array = mdot1 / (4*math.pi*(np.square(radArray))*vel) # kg/m^3
den2Array = mdot2 / (4*math.pi*(np.square(radArray))*vel) # kg/m^3

#print(den1Array[-1])
#print(mdot1)
#print(rf)

denFactor = 1.673e-24 # g/hydrogen
radFactor = 3.086e18 # cm/pc

#initialDen = (mdot1/(4*math.pi*(ri**2)*vel))/denFactor # ((g/s)/(cm^3/s)) = (g/cm^3) / (g/H) = H/cm^3
#finalDen = (mdot1/(4*math.pi*(rf**2)*vel))/denFactor

#print("initial density at 10 AU is {} H/cm^3".format(initialDen))
#print("final density at 14.348 pc is {} H/cm^3".format(finalDen))

normDen1Array = np.divide(den1Array,denFactor) # hydrogen /cm^3
normDen2Array = np.divide(den2Array,denFactor) # hydrogen /cm^3
normRadArray = np.divide(radArray,radFactor) # pc

pointPair1List = list()
pointPair2List = list()
for num in range(len(radArray)):
	radValue = radArray[num]
	den1Value = normDen1Array[num]
	den2Value = normDen2Array[num]
	
	pair1 = radValue,den1Value
	pair2 = radValue,den2Value
	
	pointPair1List.append(pair1)
	pointPair2List.append(pair2)

#print(pointPair1List)

# scale it artificially to match a final density of 2 cm^-3
# if I am artificially scaling it there is no point to doing 10^-6 vs. 10^-7, as I am scaling the difference away
#scaleFactor1 = hden / normDen1Array[-1]
#scaleFactor2 = hden / normDen2Array[-1]

#scaledDen1Array = normDen1Array * scaleFactor1
#scaledDen2Array = normDen2Array * scaleFactor2
"""
plt.scatter(normRadArray[0:],normDen1Array[0:],color="red",label="Mdot=1e-6",s=10)
plt.scatter(normRadArray[0:],normDen2Array[0:],color="blue",label="Mdot=1e-7",s=6)
plt.xlabel("Radius [pc]")
plt.ylabel("Density profile [H/cm^3]")
#plt.xscale("log")
plt.yscale("log")
plt.title("Density profile of calculateBBDensityProfile.py")
plt.legend()
plt.show()
"""
