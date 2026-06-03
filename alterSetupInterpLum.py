# the goal of this script is to set up the arrays needed for interpLum

# import packages
import matplotlib.pyplot as plt
import numpy as np

tempList = [30000,100000,300000,700000,1000000]
lumList = [36,36.5,37,37.5,38]
hdenList = [2.0]
distList = [2300,2500,2800]

paramList = list()
paramArrayList = list()

r = 19.646190595492143
neutralFrac = 0.5
dist = 2500
hden = 2.0

#for hden in hdenList:
	
# for given distance set a radius
if dist == 2300:
	rad = 13.200
if dist == 2500:
	rad = 14.348
if dist == 2800:
	rad = 16.070

ovrfile = "2dBBgridTable_vacuum_h"+str(hden)+"_d"+str(dist)+"_GASS_sublim_IUC.ovr"
pairs = list() # items are tuples of (temp,lum)

# create quartets of all parameter combinations

for temp in tempList:
	for lum in lumList:
	
		tup = temp,lum
		pairs.append(tup)
#print(pairs)
# need to parse through the .ovr file

ovr2D = open('../cloudyCode/'+ovrfile,'r')

breaksList = list() # this will be a set of numbers where every pair are the deliniations between the next grid
lineCounter = 1

# add the grid breaks to the list breaksList
for line in ovr2D:
	
	if not line[0].isnumeric():
		
		breaksList.append(lineCounter)
		
	lineCounter += 1

pairCounter = 0

ovr2D.close()
#print("breaksList is {}".format(breaksList))

# for each temp,lum combo
for pair in pairs:

	# pull from the appropriate part of the 2dBBgrid.ovr file via the breaksList values
	#print(pairCounter)
	"""
	if pairCounter == 0: # there is a non-numeric line at the beginning
		start = breaksList[0]
		stop = breaksList[1]
	else:
		start = breaksList[pairCounter-1]+1 # we don't want to include the value given (this is a non-numeric line)
		stop = breaksList[pairCounter] # next value in breaksList, will not be included (endpoint)
	"""	
	start = breaksList[pairCounter]+1
	stop = breaksList[pairCounter+1]-1
	
	ovr2D = open('../cloudyCode/'+ovrfile,'r')
	pairOvr = open("individualPair.txt","w")
	
	lineCounter = 1
	for line in ovr2D:
	
		# section of 2dBBgrid.ovr with the values related to this pair
		if (lineCounter >= start) and (lineCounter <= stop): 
		
			pairOvr.write(line)
	
		lineCounter += 1
	
	# set initial conditions
	depth = list()
	radius = list()
	density = list()
	hi = list()
	hii = list()
	hfrac = list()
	
	pairOvr.close()
	
	pairOvr = open("individualPair.txt","r")
	
	for line in pairOvr:

		# get rid of the first line and grid delineating lines
		if line[0].isnumeric():
			nums = line.split("\t")
			depth.append(nums[0])
			density.append(float(nums[3]))
			hi.append(nums[6])
			hii.append(nums[7])

	# make ionization fraction
	for value in range(0,int(len(depth))):
		
		if (float(hii[value])+float(hi[value])) == 0:
			print("The sum of the neutral and ionized hydrogen are zero at h={} d={} T={} L={}.".format(hden,dist,pair[0],pair[1]))
			hfrac.append(0) 
		else:
			frac = float(hii[value])/(float(hii[value])+float(hi[value]))
			hfrac.append(frac)
	    
	# make depth (distance from illuminating face) into radius (distance from geometric center)
	for value in depth:
		radius.append((float(value)+float(10**r))/(3.086e+18))

	# make into arrays
	radiusArray = np.array(radius)
	ionArray = np.array(hfrac)	
	hdenArray = np.array(density)
	normalHdenArray = np.divide(hdenArray,hden)
	
	# create tuple (hden,pair[0],pair[1],radiusArray,ionArray) = (hden,temp,lum,radiusArray,ionArray) to append to Tuple list 
	paramArrayTuple = hden,pair[0],pair[1],radius,hfrac # was radiusArray,ionArray
	paramTuple = hden,pair[0],pair[1]
	
	paramList.append(paramTuple)
	paramArrayList.append(paramArrayTuple)
	
	pairCounter += 1
	pairOvr.close()
	ovr2D.close()
	
#print(paramArrayList)

#plt.scatter(radiusArray,normalHdenArray,label="hdenArray, h={}, T={}, L={}".format(hden,pair[0],pair[1]),color="red")
#plt.scatter(radiusArray,ionArray,label="ionArray, T={}, L={}".format(pair[0],pair[1]),color="blue")
#plt.legend()
#plt.show()

