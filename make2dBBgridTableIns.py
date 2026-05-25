# the goal of this script is to create the 45 (5 temp x 3 dist x 3 hden) in scripts necessary to test how well they all fit to 50% neutral fraction
# so as it turns out this generated the wrong files and they don't align with interpLum which I should've checked but didn't

import shutil

#tempList = [30000,100000,300000,700000,1000000]
#lumList = [36,36.5,37,37.5,38]
hdenList = [0.75,2.0,5.0]
distList = [2300,2500,2800]

#gridTableList = [5.489395921727129,-28.35769933714156,19.6099784228377,-0.12493873660829993,20,-0.12493873660829993,5.489395921727129,-28.43852808413833,
#19.646190595492143,-0.12493873660829993,20,-0.12493873660829993,5.489395921727129,-28.536964129478694,19.695408618162325,-0.12493873660829993,20,
#-0.12493873660829993,5.489395921727129,-27.94013500655716,19.6099784228377,0.3010299956639812,20,0.3010299956639812,5.489395921727129,
#-28.01255935186605,19.646190595492143,0.3010299956639812,20,0.3010299956639812,5.489395921727129,-28.110995397206413,19.695408618162325,
#0.3010299956639812,20,0.3010299956639812,5.489395921727129,-27.542194997885122,19.6099784228377,0.6989700043360189,20,0.6989700043360189,
#5.489395921727129,-27.61461934319401,19.646190595492143,0.6989700043360189,20,0.6989700043360189,5.489395921727129,-27.713055388534375,
#19.695408618162325,0.6989700043360189,20,0.6989700043360189]

for hden in hdenList:
	for dist in distList:
	
		if dist == 2300:
			rad = 19.6099784228377
		if dist == 2500:
			rad = 19.646190595492143
		if dist == 2800:
			rad = 19.695408618162325
	
		if hden == 0.75:
			h2 = -0.12493873660829993
			h3 = -0.12493873660829993
			
			if dist == 2300:
				h1 = -28.35769933714156
			if dist == 2500:
				h1 = -28.43852808413833
			if dist == 2800:
				h1 = -28.536964129478694
			
		if hden == 2.0:
			h2 = 0.3010299956639812
			h3 = 0.3010299956639812
		
			if dist == 2300:
				h1 = -27.94013500655716
			if dist == 2500:
				h1 = -28.01255935186605
			if dist == 2800:
				h1 = -28.110995397206413
		
		if hden == 5.0:
			h2 = 0.6989700043360189
			h3 = 0.6989700043360189
			
			if dist == 2300:
				h1 = -27.542194997885122
			if dist == 2500:
				h1 = -27.61461934319401
			if dist == 2800:
				h1 = -27.713055388534375
	
		rad1 = 5.489395921727129
		rad2 = rad
		rad3 = 20

		
		line1 = "continue " + str(rad1) + " " + str(h1)
		line2 = "continue " + str(rad2) + " " + str(h2)
		line3 = "continue " + str(rad3) + " " + str(h3)
		
		inName = "2dBBgridTable" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
		
		inFile = open(inName,"w")
		
		inFile.write("blackbody 30000 vary" + "\n")
		inFile.write('grid list "temp.gridlist" linear sequential' + "\n")
		inFile.write("luminosity 36 vary" + "\n")
		inFile.write('grid list "lum.gridlist" sequential' + "\n")
		inFile.write("radius 13" + "\n")
		inFile.write("stop radius 19.99" + "\n")
		inFile.write("sphere" + "\n")
		inFile.write("abundances ISM no grains" + "\n")
		inFile.write("grains GASS function sublimation" + "\n")
		inFile.write("dlaw table" + "\n")
		inFile.write(line1 + "\n")
		inFile.write(line2 + "\n")
		inFile.write(line3 + "\n")
		inFile.write("end of dlaw" + "\n")
		inFile.write("iterate until convergence" + "\n")
		inFile.write('save overview "2dBBgridTable' + '_h' + str(hden) + '_d' + str(dist) + '_GASS_sublim_IUC.ovr" last' + "\n")
		
		inFile.close()
			
			
for hden in hdenList:
	for dist in distList:
		
		inName = "2dBBgridTable" + "_h" + str(hden) + "_d" + str(dist) + "_GASS_sublim_IUC.in"
		destination = "../cloudyCode"
		dest = shutil.move(inName,destination)
		
		
