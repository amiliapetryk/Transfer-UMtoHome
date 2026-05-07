# the goal of this script is to plot the outputs of the 2d temp lum BB grids with variable density (e.g. 2dBBgridTable_h0.75_d2300.ovr

# import packages
import matplotlib.pyplot as plt
import numpy as np

tempList = [30000,100000,300000,700000,1000000]
lumList = [36,36.5,37,37.5,38]

hden = "0.75"
dist = "2300"
r = "15"

if dist == "2300":
	rad = 13.200
if dist == "2500":
	rad = 14.348
if dist == "2800":
	rad = 16.070

ovrfile = "2dBBgridTable_h"+hden+"_d"+dist+"_r"+r+".ovr"
rad = 12

pairs = list() # items are tuples of (temp,lum)

# create quartets of all parameter combinations

for temp in tempList:
	for lum in lumList:
	
		tup = temp,lum
		pairs.append(tup)

# need to parse through the .ovr file

ovr2D = open('../cloudyCode/'+ovrfile,'r')

breaksList = list() # this will be a set of numbers where every pair are the deliniations between the next grid
lineCounter = 1

for line in ovr2D:
	
	if not line[0].isnumeric():
		
		breaksList.append(lineCounter)
		
	lineCounter += 1

pairCounter = 0

ovr2D.close()

for pair in pairs:

	# pull from the appropriate part of the 2dBBgrid.ovr file via the breaksList values
	#print(pairCounter)
	if pairCounter == 0: # there is no non-numeric line at the beginning
		start = 0
		stop = breaksList[0]
	else:
		start = breaksList[pairCounter-1]+1 # we don't want to include the value given (this is a non-numeric line)
		stop = breaksList[pairCounter] # next value in breaksList, will not be included (endpoint)
	
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
			hi.append(nums[6])
			hii.append(nums[7])

	# make ionization fraction
	for value in range(0,int(len(depth))):
		
		if (float(hii[value])+float(hi[value])) == 0:
			#print("The sum of the neutral and ionized hydrogen are zero.")
			hfrac.append(0) 
		else:
			frac = float(hii[value])/(float(hii[value])+float(hi[value]))
			hfrac.append(frac)
	    
	# make depth (distance from illuminating face) into radius (distance from geometric center)
	for value in depth:
		radius.append((float(value)+float(10**rad))/(3.086e+18))

	# make into arrays
	radiusArray = np.array(radius)
	ionArray = np.array(hfrac)	
	
	if pair[1] == 36:
		mark='x'
	elif pair[1] == 36.5:
		mark='_'
	elif pair[1] == 37:
		mark='s'
	elif pair[1] == 37.5:
		mark='.'
	else:	# L=38
		mark='^'
		
	if pair[0] == 1000000:
		colour="firebrick"
	elif pair[0] == 700000:
		colour="darkorange"
	elif pair[0] == 300000:
		colour="gold"
	elif pair[0] == 100000:
		colour="limegreen"
	else:	# T=1000000
		colour="deepskyblue"

	plt.scatter(radiusArray,ionArray,label="T={}, L={}".format(pair[0],pair[1]),s=8,color=colour,marker=mark)
	
	pairCounter += 1
	ovr2D.close()

# add point of ionization fraction that presumably is going to come from Parviz at some poitn maybe who knows
neutralFrac = 0.5 
ionFrac = 1 - neutralFrac
location = rad # location of slit (and therefore broad/narrow measurement)
"""
plt.arrow(rad,0.5,0,-0.1,head_width=0.05,head_length=0.05,ec="black",fc="black")
plt.plot([rad-0.03,rad+0.03],[0.501,0.501],color="black",linewidth=1,label="Temp. equil. constraint")
"""	
plt.title("2D BB with power law density at h={} and d={}".format(hden,dist))
plt.xlabel("Radius [parsec]")
plt.ylabel("Ionization Fraction (HII/(HI + HII))")
plt.legend(fontsize=8)
plt.show()

