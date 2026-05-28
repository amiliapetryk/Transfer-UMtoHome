# the goal of this script is to create the 1 (2.0 and 2500) 2dBB grid in scripts necessary to test how well they all fit to 50% neutral fraction

import shutil

hden= 2.0
distList = 2500
rad = 19.646190595492143
		
inName = "2dBBgrid_vacuum" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
		
inFile = open(inName,"w")

inFile.write("blackbody 30000 vary" + "\n")
inFile.write('grid list "temp.gridlist" linear sequential' + "\n")
inFile.write("luminosity 36 vary" + "\n")
inFile.write('grid list "lum.gridlist" sequential' + "\n")
inFile.write("radius " + str(rad) + "\n")
inFile.write("stop radius 19.99" + "\n")
inFile.write("sphere" + "\n")
inFile.write("abundances ISM no grains" + "\n")
inFile.write("grains GASS function sublimation" + "\n")
inFile.write("hden " + str(hden) + " linear" + "\n")
inFile.write("iterate until convergence" + "\n")
inFile.write('save overview "2dBBgrid_vacuum' + '_h' + str(hden) + '_d' + str(dist) + '_GASS_sublim_IUC.ovr" last' + "\n")

inFile.close()
		
inName = "2dBBgrid_vacuum" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
destination = "../cloudyCode"
dest = shutil.move(inName,destination)
