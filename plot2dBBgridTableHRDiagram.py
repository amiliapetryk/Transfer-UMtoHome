# the goal of this script is to take the temp,lum pairs calculated by interpLum.py and plot an HR diagram accordingly

import matplotlib.pyplot as plt
import numpy as np
import alterSetupInterpLum

d2300LumValues = [36.0, 36.0, 36.435403920772714, 37.09087136714792, 37.42693953016554, 36.715594335795316, 36.823301147746825, 37.180241877476135, 37.750175678682254, 38.0, 37.4995413685652, 37.62081075906676, 37.923631989384184, 38.0, 38.0]
d2500LumValues = [36.0, 36.04845787173087, 36.52505677571444, 37.17982965790094, 37.497916557201386, 36.83065313719807, 36.91712995716621, 38.0, 37.84637671816081, 38.0, 37.635922416922035, 37.744342120403395, 38.0, 38.0, 38.0]
d2800LumValues = [36.06751550496452, 36.21566853046389, 36.66754693541477, 37.30919398300366, 37.625064367297185, 36.95924661698511, 37.054062348927616, 37.42078560402868, 37.9669825208715, 38.0, 37.80215709535248, 37.89217244862604, 38.0, 38.0, 38.0]

#temp0 = 30000
#temp1 = 100000
#temp2 = 300000
#temp3 = 700000
#temp4 = 1000000

tempList = [30000,100000,300000,700000,1000000]

dist = 2500

if dist == 2300:
	modifier = 0
	lumValues = d2300LumValues
if dist == 2500:
	modifier = 1
	lumValues = d2500LumValues
if dist == 2800:
	modifier = 2
	lumValues = d2800LumValues
	
counter = 0
masterLowHList = list()
masterMidHList = list()
masterHighHList = list()

fig, ax = plt.subplots()

for temp in tempList:
	
	lowHLum = lumValues[counter]
	midHLum = lumValues[counter+5]
	highHLum = lumValues[counter+10]
	
	if counter == 0:
		colour="firebrick"
	if counter == 1:
		colour="darkorange"
	if counter == 2:
		colour="limegreen"
	if counter == 3:
		colour="deepskyblue"
	if counter == 4:
		colour="darkorchid"
		
	lowLumList = list()
	midLumList = list()
	highLumList = list()
	
	if lowHLum >= 36.001 and lowHLum <= 37.999:
		lowLumList.append(lowHLum)
		tempLum = temp,lowHLum
		masterLowHList.append(tempLum)

	if midHLum >= 36.001 and midHLum <= 37.999:
		midLumList.append(midHLum)
		tempLum = temp,midHLum
		masterMidHList.append(tempLum)
		
	if highHLum >= 36.001 and highHLum <= 37.999:
		highLumList.append(highHLum)
		tempLum = temp,highHLum
		masterHighHList.append(tempLum)
		
	lumCounter = 0	
	for item in lowLumList:	
		ax.scatter(temp,lowLumList[lumCounter],marker='x',color=colour,s=128,label="T={} K, hden=0.75 cm$^-$$^3$".format(temp))
		lumCounter += 1
		
	lumCounter = 0
	for item in midLumList:
		ax.scatter(temp,midLumList[lumCounter],marker='o',color=colour,s=128,label="T={} K, hden=2.0 cm$^-$$^3$".format(temp))
		lumCounter += 1

	lumCounter = 0
	for item in highLumList:
		ax.scatter(temp,highLumList[lumCounter],marker='s',color=colour,s=128,label="T={} K, hden=5.0 cm$^-$$^3$".format(temp))
		lumCounter += 1
		
	#print("counter is {}".format(counter))
	counter += 1

# play connect the dots
smallLowTempList = list()
smallLowLumList = list()
for pair in masterLowHList:
	smallLowTempList.append(pair[0])
	smallLowLumList.append(pair[1])

ax.plot(smallLowTempList,smallLowLumList,color="gray",linestyle="dotted",label="Upper limit for h=0.75 cm$^-$$^3$")	

smallMidTempList = list()
smallMidLumList = list()
for pair in masterMidHList:
	smallMidTempList.append(pair[0])
	smallMidLumList.append(pair[1])

ax.plot(smallMidTempList,smallMidLumList,color="gray",linestyle="dashed",label="Upper limit for h=2.0 cm$^-$$^3$")

smallHighTempList = list()
smallHighLumList = list()
for pair in masterHighHList:
	smallHighTempList.append(pair[0])
	smallHighLumList.append(pair[1])

ax.plot(smallHighTempList,smallHighLumList,color="gray",linestyle="solid",label="Upper limit for h=5.0 cm$^-$$^3$")		
	
#plt.plot(tempList,midLumList,color="gray",linestyle="dashed",label="Upper limit for h=2.0")
#plt.plot(tempList,highLumList,color="gray",linestyle="solid",label="Upper limit or h=5.0")
	
	
ax.set_xlabel("Temperature $\u22C5$ 10$^6$ [K]",size=20)
ax.tick_params(axis="both",labelsize=20)
ax.set_ylabel("log(Luminosity[erg/s])",size=20)	
#plt.title("HR diagram for Cloudy BB plots for distance of {} pc".format(dist))
ax.set_title("Upper limits on blackbody progenitor of RCW 86, d=2500 pc",size=24)

ax.text(0,37.38,"Upper limit for h=5.0 cm$^-$$^3$",rotation=29.6,fontsize=20)
ax.text(200000,36.97,"Upper limit for h=2.0 cm$^-$$^3$",rotation=29.6,fontsize=20)
ax.text(350000,36.52,"Upper limit for h=0.75 cm$^-$$^3$",rotation=29.6,fontsize=20)

#ax.legend(fontsize="large")
plt.show()
	
	
	
"""
# import lum values (list according to h=0.75,2.0,5.0)
hrT30000d2300Values = interpLum.hrT30000d2300Values
hrT30000d2500Values = interpLum.hrT30000d2500Values
hrT30000d2800Values = interpLum.hrT30000d2800Values

hrT100000d2300Values = interpLum.hrT100000d2300Values
hrT100000d2500Values = interpLum.hrT100000d2500Values
hrT100000d2800Values = interpLum.hrT100000d2800Values

hrT300000d2300Values = interpLum.hrT300000d2300Values
hrT300000d2500Values = interpLum.hrT300000d2500Values
hrT300000d2800Values = interpLum.hrT300000d2800Values

hrT700000d2300Values = interpLum.hrT700000d2300Values
hrT700000d2500Values = interpLum.hrT700000d2500Values
hrT700000d2800Values = interpLum.hrT700000d2800Values

hrT1000000d2300Values = interpLum.hrT1000000d2300Values
hrT1000000d2500Values = interpLum.hrT1000000d2500Values
hrT1000000d2800Values = interpLum.hrT1000000d2800Values

masterList = [hrT30000d2300Values,hrT30000d2500Values,hrT30000d2800Values,hrT100000d2300Values,hrT100000d2500Values,
hrT100000d2800Values,hrT300000d2300Values,hrT300000d2500Values,hrT300000d2800Values,hrT700000d2300Values,hrT700000d2500Values,
hrT700000d2800Values,hrT1000000d2300Values,hrT1000000d2500Values,hrT1000000d2800Values]
"""	
	
"""
# these are 3 lists (hden = 0.75, 2.0, 5.0) containing 5 values for T=30,000, 100,000, 300,000, 700,000, 1,000,000
lum0 = lumValues[modifier:5+modifier]
lum1 = lumValues[5+modifier:10+modifier]
lum2 = lumValues[10+modifier:] # should go until the end of the list
#lum3 = lumValues[15+modifier]
#lum4 = lumValues[20+modifier]

# this is a list of lists	
lumList = [lum0,lum1,lum2]#,lum3,lum4]	
"""	
	
	
