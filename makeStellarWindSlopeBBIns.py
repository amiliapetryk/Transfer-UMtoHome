# make 2 2d BB grid with the density profile (one for Mdot=10-6 and one for Mdot=10-7) as governed by the equation of stellar structure

import calculateBBDensityProfile
import shutil
import math
import numpy as np

pointPair1List = calculateBBDensityProfile.pointPair1List # list of tuples (x,y) = (radius,density) for mdot=10e-6
pointPair2List = calculateBBDensityProfile.pointPair2List # list of tuples (x,y) = (radius,density) for mdot=10e-7

hden= 2.0
dist = 2500
#ri = calculateBBDensityProfile.ri
#rf = calculateBBDensityProfile.rf
rad = 19.646190595492143
shockWidth = 17.5778
shockFactor = 10
linSteps = 20

start1 = math.log10(pointPair1List[0][0]+1)
ri1 = math.log10(pointPair1List[0][0]) # select the first x,y pair [0] and the radius value of the pair [0] and add 1 (+1)
di1 = math.log10(pointPair1List[0][1])
rf1 = math.log10(pointPair1List[-1][0]) # should be at 14.348 pc
df1 = math.log10(pointPair1List[-1][1])
	
start2 = math.log10(pointPair2List[0][0]+1)
ri2 = math.log10(pointPair2List[0][0]) # select the first x,y pair [0] and the radius value of the pair [0] and add 1 (+1)
di2 = math.log10(pointPair2List[0][1])
rf2 = math.log10(pointPair2List[-1][0]) # should be at 14.348 pc
df2 = math.log10(pointPair2List[-1][1])

	
inName1 = "2dBBgrid_stellarWindLin_mdot1e-6" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
inName2 = "2dBBgrid_stellarWindLin_mdot1e-7" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
		
inFile1 = open(inName1,"w")
inFile2 = open(inName2,"w")

inFile1.write("blackbody 30000 vary" + "\n")
inFile1.write('grid list "temp.gridlist" linear sequential' + "\n")
inFile1.write("luminosity 36 vary" + "\n")
inFile1.write('grid list "lum.gridlist" sequential' + "\n")
inFile1.write("radius " + str(start1) + "\n")
inFile1.write("stop radius 19.99" + "\n")
inFile1.write("sphere" + "\n")
inFile1.write("abundances ISM no grains" + "\n")
inFile1.write("grains GASS function sublimation" + "\n")
inFile1.write("dlaw table" + "\n")
inFile1.write("continue " + str(ri1) + " " + str(di1) + "\n")
#inFile1.write("continue " + str(rf1) + " " + str(df1) + "\n")

# add the ramp up
linRad1 = np.logspace(rf1,math.log10(10**(rf1)+10**(shockWidth)/shockFactor),linSteps)
linDen1 = np.logspace(df1,math.log10(hden),linSteps)

for num in range(len(linRad1)):
	inFile1.write("continue " + str(math.log10(linRad1[num])) + " " + str(math.log10(linDen1[num])) + "\n")

#inFile1.write("continue " + str(math.log10(10**(rf1)+10**(shockWidth)/shockFactor)) + " " + str(math.log10(hden)) + "\n")
inFile1.write("continue 20 " + str(math.log10(hden)) + "\n")
inFile1.write("end of dlaw" + "\n")
inFile1.write("iterate until convergence" + "\n")
inFile1.write('save overview "2dBBgrid_stellarWindLin' + '_h' + str(hden) + '_d' + str(dist) + '_GASS_sublim_IUC.ovr" last' + "\n")

inFile1.close()

inFile2.write("blackbody 30000 vary" + "\n")
inFile2.write('grid list "temp.gridlist" linear sequential' + "\n")
inFile2.write("luminosity 36 vary" + "\n")
inFile2.write('grid list "lum.gridlist" sequential' + "\n")
inFile2.write("radius " + str(start2) + "\n")
inFile2.write("stop radius 19.99" + "\n")
inFile2.write("sphere" + "\n")
inFile2.write("abundances ISM no grains" + "\n")
inFile2.write("grains GASS function sublimation" + "\n")
inFile2.write("dlaw table" + "\n")
inFile2.write("continue " + str(ri2) + " " + str(di2) + "\n")
#inFile2.write("continue " + str(rf2) + " " + str(df2) + "\n")

# add the ramp up
linRad2 = np.logspace(rf2,math.log10(10**(rf2)+10**(shockWidth)/shockFactor),linSteps)
linDen2 = np.logspace(df2,math.log10(hden),linSteps)

for num in range(len(linRad2)):
	inFile2.write("continue " + str(math.log10(linRad2[num])) + " " + str(math.log10(linDen2[num])) + "\n")

#inFile2.write("continue " + str(math.log10(10**(rf2)+10**(shockWidth)/shockFactor)) + " " + str(math.log10(hden)) + "\n")
inFile2.write("continue 20 " + str(math.log10(hden)) + "\n")
inFile2.write("end of dlaw" + "\n")
inFile2.write("iterate until convergence" + "\n")
inFile2.write('save overview "2dBBgrid_stellarWind' + '_h' + str(hden) + '_d' + str(dist) + '_GASS_sublim_IUC.ovr" last' + "\n")

inFile2.close()
	
inName1 = "2dBBgrid_stellarWindLin_mdot1e-6" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
inName2 = "2dBBgrid_stellarWindLin_mdot1e-7" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
destination = "../cloudyCode"
dest1 = shutil.copy(inName1,destination)
dest2 = shutil.copy(inName2,destination)
