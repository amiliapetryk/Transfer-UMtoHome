import os
import math
import shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# move to the metallicity = 0.014 gotberg directory
toGrid014 = "../gotberg/grid_014"
grid014 = os.chdir(toGrid014)

# (mass,luminosity,effective radius,wind mass loss rate,terminal wind speed)
gotbergParamList = [(2.0,0.6,0.16,-12.0,1370),(2.21,0.8,0.17,-12.0,1380),(2.44,1.1,0.19,-12.0,1420),(2.7,1.4,0.21,-12.0,1440),(2.99,1.6,0.23,-12.0,1480),(3.3,1.9,0.25,-12.0,1510),(3.65,2.0,0.26,-12.0,1570),(4.04,2.3,0.29,-11.2,1590),(4.46,2.5,0.32,-10.6,1610),(4.93,2.7,0.36,-10.0,1630),(5.45,2.9,0.4,-9.5,1660),(6.03,3.0,0.42,-8.4,1720),(6.66,3.2,0.46,-8.1,1750),(7.37,3.4,0.5,-7.8,1800),(8.15,3.6,0.55,-7.5,1850),(9.0,3.8,0.59,-7.3,1900),(9.96,3.9,0.65,-7.1,1950),(11.01,4.1,0.7,-6.8,2020),(12.17,4.3,0.76,-6.6,2100),(13.45,4.4,0.8,-6.4,2190),(14.87,4.6,0.84,-6.2,2300),(16.44,4.7,0.87,-6.0,2420),(18.17,4.9,0.88,-5.8,2570)]

colourList = ["lightpink","lightcoral","indianred","tomato","darkred","sandybrown","darkorange","goldenrod","gold","yellow","yellowgreen","olivedrab","darkgreen",
"mediumseagreen","springgreen","aquamarine","turquoise","lightseagreen","paleturquoise","cyan","deepskyblue","royalblue","mediumslateblue","darkviolet",
"mediumorchid","violet","hotpink","deeppink","mediumvioletred","crimson"]

dist = 2500
hden = 2.0
rad = 19.646190595492143

dirList = list()

for root, dirs, files in os.walk('.'): # root = current directory (looping), dirs = directories in current directory, files = files in current directory

	if len(root) >= 3: # if we're not in the root directory
		dirName = root[2:]
		dirList.append(dirName)

# go back to pythonCode directory
backDir = os.chdir("../../pythonCode")

# loop through each directory and perform the desired copying (same as fetchGotbergSED.py)
colourCounter = 0
for model in dirList:

	modelName = model

	num = 0
	initial = True
	for char in modelName:

		if char == "_" and initial:
			mMarker = num
			initial = False
			
		if char == "q":
			qMarker = num
		
		if char == "P":
			pMarker = num
			
		if char == "Z":
			zMarker = num
			
		if char == "_" and not initial:
			endMarker = num
			
		num += 1
		
	mass = modelName[mMarker+1:qMarker]
	period = modelName[pMarker+1:zMarker]
	metal = modelName[zMarker+1:endMarker]
	smallMetal = modelName[zMarker+3:endMarker]
	
	for group in gotbergParamList:
		if float(mass) == float(group[0]):
			modelMass = group[0]
			lum = group[1]
			effRad = group[2]
			massLossLog = group[3]
			massLoss = (10**massLossLog) * 1.989e33 * (1/31557600) # solar mass/yr * g/solar mass * yr/s = g/s
			termWind = group[4] * 100000 # km/s * 100000 cm/km = cm/s
			
#			if float(mass) == 6.03:
#				print(termWind)

	# we have the lum required, write the in files
	inName = modelName + "_stellarWind_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
	inFile = open(inName,"w")
	
	# calculate density profile to input
	ri = effRad * 69570000000 # solar rad * cm/solar rad = cm
	rf = 10**19.99 # cm
	num = 1000
	radArray = np.logspace(math.log10(ri),math.log10(rf),num)
	velArray = termWind*(1-(ri/radArray))
	denArray = massLoss/(4*math.pi*np.square(radArray)*termWind) # (g/s)/(cm^3/s) = g/cm^3
	
#	if float(mass) == 6.03:
#		print(radArray)
#		print("ri is {}".format(ri))
#		print("radArray is {}".format(radArray))
#		print("ri/radArray is {}".format(ri/radArray))
#		print("velArray is {}".format(velArray))
#		print("{:.8f}".format(velArray[0]))
#		print("{:.8f}".format(velArray[-1]))
	
	pcRadArray = radArray/3.086e18
	kmVelArray = velArray/100000
	hDenArray = denArray/1.673e-24 # g/cm^3 * H/1.673e-24g = = H/cm^3 
	
	# fit data to quadratics
	# fix this
	if float(mass) == 6.03:
		def quad(x,a,b,c):
			return a*x**2 + b*x + c
			
		popt,pcov=curve_fit(quad,radArray,hDenArray)
		a,b,c = popt
		print("a is {}".format(a))
		print("b is {}".format(b))
		print("c is {}".format(c))
		
		xData = radArray
		yData = quad(xData,a,b,c)
		
		#plt.scatter(pcRadArray,kmVelArray,color=colourList[colourCounter],marker="o",label="wind velocity for M={}".format(modelMass),s=6)
		plt.scatter(radArray,hDenArray,color=colourList[colourCounter],marker="x",label="hden profile for M={}".format(modelMass),s=6)
		plt.plot(xData,yData,color=colourList[colourCounter],linestyle=":")
	
	colourCounter += 1
	
plt.xlabel("Radius [pc]")
plt.ylabel("Wind velocity [km/s] or hden profile [H/cm^3]")
plt.xscale("log")
#plt.yscale("log")
plt.title("Tests for gotberg stellar wind parameters")
plt.legend()
plt.show()
