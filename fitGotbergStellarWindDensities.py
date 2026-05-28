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

fittedParamList = [('2.0', np.float64(2.188287824120634e+28)), ('2.99', np.float64(2.025644810165719e+28)), ('5.45', np.float64(5.711062632121788e+30)), ('8.15', np.float64(5.124521064498456e+32)), ('18.17', np.float64(1.8488083235658514e+34)), ('7.37', np.float64(2.6396874397579135e+32)), ('16.44', np.float64(1.2388240987790356e+34)), ('6.66', np.float64(1.3607770068750074e+32)), ('2.21', np.float64(2.172430665974827e+28)), ('12.17', np.float64(3.5859622744263645e+33)), ('4.46', np.float64(4.6773420970778604e+29)), ('13.45', np.float64(5.44980416166094e+33)), ('4.93', np.float64(1.8392357785553762e+30)), ('14.87', np.float64(8.22426650442489e+33)), ('9.96', np.float64(1.2212101343750067e+33)), ('9.0', np.float64(7.90808648264857e+32)), ('2.44', np.float64(2.11123543594737e+28)), ('3.65', np.float64(1.9095250439778766e+28)), ('3.3', np.float64(1.985400211288257e+28)), ('6.03', np.float64(6.9389948337427e+31)), ('4.04', np.float64(1.1896737710803316e+29)), ('11.01', np.float64(2.3521967284971474e+33)), ('2.7', np.float64(2.081912721559215e+28))]

massPointList = list()

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
#	print("mass is {}".format(mass))
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
	rf = 10**20 # cm
	num = 1000
	radArray = np.logspace(math.log10(ri),math.log10(rf),num)
	smallRadArray = radArray[1:] # for some arrays the first value leads to infinite density
	velArray = termWind*(1-(ri/smallRadArray))	
	denArray = massLoss/(4*math.pi*np.square(smallRadArray)*velArray) # (g/s)/(cm^3/s) = g/cm^3
	#denArray = massLoss/(4*math.pi*np.square(smallRadArray)*termWind) # this one works and above doesn't
	#smallDenArray = denArray[1:]

	pcRadArray = smallRadArray/3.086e18
	kmVelArray = velArray/100000
	hDenArray = denArray/1.673e-24 # g/cm^3 * H/1.673e-24g = = H/cm^3 

#	def invQuad(x,k,d):
#		return k/((x-d)**2)
		
	def powerLaw(x,k):
		return k/(x*(x-ri)) # 2 cm-3 
		
	for group in fittedParamList:
		if float(mass) == float(group[0]):
			initial_k = group[1]
	#		initial_d = group[2]
	
	initial_guess = [initial_k]
		
	popt,pcov=curve_fit(powerLaw,smallRadArray,hDenArray,p0=initial_guess)
	#k,d = popt
	k = popt
	fitTuple = mass,k[0]
	fittedParamList.append(fitTuple)
	
	xData = smallRadArray
	#yData = invQuad(xData,k,d)
	yData = powerLaw(xData,k)
	
	# this is a list of point that fit the density profile that can be linearly interpolated betweel in loglog space
	pointList = list()
	for num in range(len(xData)):
		point = xData[num],yData[num]
		pointList.append(point)
	massPointListTuple = mass,pointList
	massPointList.append(massPointListTuple)
	
	colourCounter += 1




#plt.scatter(pcRadArray,kmVelArray,color=colourList[colourCounter],marker="o",label="wind velocity for M={}".format(modelMass),s=6)
#plt.scatter(smallRadArray,hDenArray,color=colourList[colourCounter],marker="x",label="hden profile for M={}".format(modelMass),s=6)
#plt.plot(xData,yData,color="black",linestyle=":")
#plt.plot(pcRadArray,yData,color="black",linestyle=":")

#print(massPointList)	
#print(fitParamList)
	
#plt.xlabel("Radius [pc]")
#plt.ylabel("Wind velocity [km/s] or hden profile [H/cm^3]")
#plt.xscale("log")
#plt.yscale("log")
#plt.title("Tests for gotberg stellar wind parameters")
#plt.legend()
#plt.show()
