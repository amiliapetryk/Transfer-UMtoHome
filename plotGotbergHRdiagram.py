# make HR diagram of Gotberg models, each mass has tabulated temp and lum, the colour coat excluded vs not excluded (on dissertation slides for h=2.0, d=2500)

import math
import matplotlib.pyplot as plt

massTempLumList = [(2.0,0.6,20.4),(2.21,0.8,22.5),(2.44,1.1,25.6),(2.7,1.4,28.2),(2.99,1.6,30.9),(3.3,1.9,33.6),(3.65,2.0,36.7),(4.04,2.3,39.5),(4.46,2.5,41.9),(4.93,2.7,44.6),(5.45,2.9,47.5),(6.03,3.0,50.8),(6.66,3.2,54.1),(7.37,3.4,57.5),(8.15,3.6,61.6),(9.0,3.8,65.5),(9.96,3.9,69.1),(11.01,4.1,73.7),(12.17,4.3,78.3),(13.45,4.4,83.4),(14.87,4.6,88.8),(16.44,4.7,94.6),(18.17,4.9,101.3)]

colourList = ["lightpink","lightcoral","indianred","tomato","darkred","sandybrown","darkorange","goldenrod","gold","yellowgreen","olivedrab","darkgreen",
"mediumseagreen","springgreen","aquamarine","turquoise","lightseagreen","paleturquoise","cyan","deepskyblue","royalblue","mediumslateblue","darkviolet",
"mediumorchid","violet","hotpink","deeppink","mediumvioletred","crimson","indigo"]

fig, ax = plt.subplots()

colourCounter = 0
for triple in massTempLumList:
	mass = triple[0] # M_solar
	gotLum = triple[1] # log(L) # L_solar
	gotTemp = triple[2] # kK
	
	lum = math.log10(10*(gotLum) * 3.828000e+33) # log(erg/s)
	temp = 1000 * gotTemp # K
	
	if mass > 4.0:
		mfc = "none"
	else:
		mfc = colourList[colourCounter]
	
	ax.scatter(temp/100000,lum,label="M={} $M_\u2609$".format(mass),color=colourList[colourCounter],facecolor=mfc,s=64)
	if colourCounter % 2 == 0 and colourCounter <= 12:
		ax.text((temp/100000)+0.01,lum-0.018,"M={} $M_\u2609$".format(mass),fontsize=18)
	elif colourCounter > 12 and (colourCounter-12) % 3 == 0:
		ax.text((temp/100000)-0.01,lum-0.037,"M={} $M_\u2609$".format(mass),fontsize=18)
		"""
		if colourCounter == 18:
			ax.text((temp/100000)-0.01,lum-0.035,"M={} $M_\u2609$".format(mass),fontsize=18)
		elif colourCounter == 20:
			ax.text((temp/100000)-0.02,lum-0.035,"M={} $M_\u2609$".format(mass),fontsize=18)
		elif colourCounter == 22:
			#ax.text((temp/100000)-0.02,lum-0.035,"M={} $M_\u2609$".format(mass),fontsize=16)
			blank = 5
		else:
			ax.text((temp/100000)+0.01,lum-0.018,"M={} $M_\u2609$".format(mass),fontsize=18)
		"""
	colourCounter += 1
	
#ax.legend(fontsize="large")
ax.text(0.19,35.25,"$\u25CF$ = model is allowed",size=20)
ax.text(0.19,35.2,"$\u25CB$ = model is not allowed",size=20)
ax.set_xlabel("Temperature $\u22C5$ 10$^5$ [K]",size=20)
ax.set_ylabel("log(Luminosity[erg/s])",size=20)
ax.tick_params(axis="both",labelsize=20)
ax.set_title("Upper limits on stripped-envelope progenitor of RCW 86, d=2500 pc",size=24)
plt.show()
