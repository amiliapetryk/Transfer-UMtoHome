# the goal of this script is to create the 45 (5 temp x 3 dist x 3 hden) in scripts necessary to test how well they all fit to 50% neutral fraction
# so as it turns out this generated the wrong files and they don't align with interpLum which I should've checked but didn't

import shutil

tempList = [30000,100000,300000,700000,1000000]
hdenList = [0.75,2.0,5.0]
#distList = [2300,2500,2800]

dist = 2500

d2300LumList = [36.0, 36.0, 36.435403920772714, 37.09087136714792, 37.42693953016554, 36.715594335795316, 36.823301147746825, 37.180241877476135, 37.750175678682254, 38.0, 37.4995413685652, 37.62081075906676, 37.923631989384184, 38.0, 38.0]

d2500LumList = [36.0, 36.04845787173087, 36.52505677571444, 37.17982965790094, 37.497916557201386, 36.83065313719807, 36.91712995716621, 38.0, 37.84637671816081, 38.0, 37.635922416922035, 37.744342120403395, 38.0, 38.0, 38.0]

d2800LumList = [36.06751550496452, 36.21566853046389, 36.66754693541477, 37.30919398300366, 37.625064367297185, 36.95924661698511, 37.054062348927616, 37.42078560402868, 37.9669825208715, 38.0, 37.80215709535248, 37.89217244862604, 38.0, 38.0, 38.0]

if dist == 2300:
	lumList = d2300LumList
	rad = 19.6099784228377
if dist == 2500:
	lumList = d2500LumList
	rad = 19.646190595492143
if dist == 2800:
	lumList = d2800LumList
	rad = 19.695408618162325

counter = 0
for hden in hdenList:
	for temp in tempList:
	
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
		
		smallLum = round(lumList[counter],3)
		
		inName = "testInterpLum_T" + str(temp) +"_L" + str(smallLum) + "_h" + str(hden) + "_d" + str(dist) + "_r13_abun_IUC.in" 
		
		inFile = open(inName,"w")
		
		inFile.write("blackbody " + str(temp) + "\n")
		inFile.write("luminosity " + str(lumList[counter]) + "\n")
		inFile.write("radius 13" + "\n")
		inFile.write("stop radius 19.99" + "\n")
		inFile.write("abundances HII region" + "\n")
		inFile.write("dlaw table" + "\n")
		inFile.write(line1 + "\n")
		inFile.write(line2 + "\n")
		inFile.write(line3 + "\n")
		inFile.write("end of dlaw" + "\n")
		inFile.write("iterate until convergence" + "\n")
		inFile.write('save overview "testInterpLum_T'+ str(temp) +'_L' + str(smallLum) + '_h' + str(hden) + '_d' + str(dist) + '_r13_abun_IUC.ovr" last' + "\n")
		
		inFile.close()
		
		counter += 1

counter = 0		
for hden in hdenList:
	for temp in tempList:
	
		smallLum = round(lumList[counter],3)
		
		inName = "testInterpLum_T" + str(temp) +"_L" + str(smallLum) + "_h" + str(hden) + "_d" + str(dist) + "_r13_abun_IUC.in" 
		destination = "../cloudyCode"
		dest = shutil.copy(inName,destination)
		
		counter += 1
		
