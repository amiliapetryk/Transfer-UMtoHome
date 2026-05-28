import fitGotbergStellarWindDensities
import os
import shutil
import math

# move to the metallicity = 0.014 gotberg directory
toGrid014 = "../gotberg/grid_014"
grid014 = os.chdir(toGrid014)

massLumList = [(2.0,0.6),(2.21,0.8),(2.44,1.1),(2.7,1.4),(2.99,1.6),(3.3,1.9),(3.65,2.0),(4.04,2.3),(4.46,2.5),(4.93,2.7),(5.45,2.9),(6.03,3.0),(6.66,3.2),(7.37,3.4),(8.15,3.6),(9.0,3.8),(9.96,3.9),(11.01,4.1),(12.17,4.3),(13.45,4.4),(14.87,4.6),(16.44,4.7),(18.17,4.9)]
dist = 2500
hden = 2.0
#ri = fitGotbergStellarWindDensities.massPointList
rf = fitGotbergStellarWindDensities.rf
#rad = math.log10(ri+1)
shockFront = 19.646190595492143
massPointList = fitGotbergStellarWindDensities.massPointList # list of (mass,pointList) tuples, for each mass (2-18.17) there is an associated list containing 1000 point pairs that trace the density profile

dirList = list()

for root, dirs, files in os.walk('.'): # root = current directory (looping), dirs = directories in current directory, files = files in current directory

	if len(root) >= 3: # if we're not in the root directory
		dirName = root[2:]
		dirList.append(dirName)

# go back to pythonCode directory
backDir = os.chdir("../../pythonCode")

# loop through each directory and perform the desired copying (same as fetchGotbergSED.py)
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
	
	# find starting radius (just in front of first point)
	for pair in massPointList:
		if float(mass) == float(pair[0]):
			ri = math.log10(pair[1][0][0]+1) # select the list of (x,y) tuple ([1]), the first x,y pair [0] and the radius value of the pair [0] and add 1 (+1)
	
	for pair in massLumList:
		if float(mass) == float(pair[0]):
			lum = pair[1]

	# we have the lum required, write the in files
	inName = modelName + "_stellarWind_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
	inFile = open(inName,"w")

	inFile.write('table SED "' + modelName + '_copy.txt"' + "\n")
	inFile.write("luminosity " + str(lum) + " solar" + "\n")
	inFile.write("radius " + str(ri) + "\n")
	inFile.write("stop radius 19.99" + "\n")
	inFile.write("sphere" + "\n")
	inFile.write("abundances ISM no grains" + "\n")
	inFile.write("grains GASS function sublimation" + "\n")
	inFile.write("dlaw table" + "\n")
	
	# this works great -> now need to cut it off at shock front and replace with hden = 2.0
	# write many lines of the dlaw table
	for pair in massPointList: # for each (mass,pointList) tuple
		if float(pair[0]) == float(mass): # if this is the tuple of the mass we're on
			for point in pair[1]: # for each (x,y)=(radius,density) point pair
				logRad = math.log10(point[0])
				logDen = math.log10(point[1])
				
				if logRad < shockFront:
					inFile.write("continue " + str(logRad) + " " + str(logDen) + "\n")
					
				else:
					inFile.write("continue " + str(logRad) + " " + str(math.log10(hden)) + "\n")
			
	
	inFile.write("end of dlaw" + "\n")
	inFile.write("iterate until convergence" + "\n")
	inFile.write('save overview "' + modelName + "_stellarWind_h" + str(hden) + "_d" + str(dist) + '_GASS_sublim_IUC.ovr" last' + "\n")
	
for model in dirList:
	modelName = model
	inName = modelName + "_stellarWind_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
	destination = "../cloudyCode"
	dest = shutil.copy(inName,destination)
