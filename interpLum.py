# the goal of this script is to determine what luminosity barely causes the CLOUDY model to barely pass through the chosen ionization fraction at the shock front for each temperature, density, and luminosity

import setupInterpLum
import numpy as np
import math

dist = setupInterpLum.dist
neutralFrac = setupInterpLum.neutralFrac # 0.5

hdenList = [0.75,2.0,5.0]
distList = [2300,2500,2800]
tempList = [30000,100000,300000,700000,1000000]
paramArrayList = setupInterpLum.paramArrayList

#print("\n")

# for given distance set a radius
if dist == 2300:
	rad = 13.200
if dist == 2500:
	rad = 14.348
if dist == 2800:
	rad = 16.070

interpLumValueList = list()

for hden in hdenList:
	for temp in tempList:
	
		sameHdenTempRadList = list()
		sameHdenTempIonList = list()
		lumList = list()
		
		for item in paramArrayList: # (hden,temp,lum,radiusArray,ionArray)

			# group the radius and ion arrays for items with the same hden and temp (varying lum)
			if item[0] == hden and item[1] == temp:
		
				# these are lists containing 5 arrays for the 5 different luminosities
				lumList.append(math.pow(10,item[2]))
				sameHdenTempRadList.append(item[3])
				sameHdenTempIonList.append(item[4])
				
		# for a particular temp and hden find the value nearest to the desired neutral fraction for each luminosity
		valueList = list()
		for array in sameHdenTempIonList:
		
			diff = 9999
		
			for num in array:
				
				indiDiff = abs(num-neutralFrac)
				
				if indiDiff < diff:
						
					# after it loops this will be the smallest distance between a point and the neutral fraction
					diff = indiDiff
					
			counter = 0
			for num in array:
			
				if abs(num-neutralFrac) == diff:
				
					valueList.append(counter)
					counter += 1
				
				else:
					counter += 1
					
		# create list of the 5 different radii and ionizations to interpolate from
		interpRadList = [sameHdenTempRadList[0][valueList[0]],sameHdenTempRadList[1][valueList[1]],sameHdenTempRadList[2][valueList[2]],sameHdenTempRadList[3][valueList[3]],sameHdenTempRadList[4][valueList[4]]]
		interpIonList = [sameHdenTempIonList[0][valueList[0]],sameHdenTempIonList[1][valueList[1]],sameHdenTempIonList[2][valueList[2]],sameHdenTempIonList[3][valueList[3]],sameHdenTempIonList[4][valueList[4]]]
			
		interpLumValue = np.interp(rad,interpRadList,lumList)
		interpLumValueList.append(math.log10(interpLumValue))
#		print("The interpolated lum value for T={},hden={},dist={} is {}.".format(temp,hden,dist,math.log10(interpLumValue)))

print(interpLumValueList)				
			
"""
The interpolated lum value for T=30000,hden=0.75,dist=2300 is 36.0.
The interpolated lum value for T=100000,hden=0.75,dist=2300 is 36.0.
The interpolated lum value for T=300000,hden=0.75,dist=2300 is 36.435403920772714.
The interpolated lum value for T=700000,hden=0.75,dist=2300 is 37.09087136714792.
The interpolated lum value for T=1000000,hden=0.75,dist=2300 is 37.42693953016554.
The interpolated lum value for T=30000,hden=2.0,dist=2300 is 36.715594335795316.
The interpolated lum value for T=100000,hden=2.0,dist=2300 is 36.823301147746825.
The interpolated lum value for T=300000,hden=2.0,dist=2300 is 37.180241877476135.
The interpolated lum value for T=700000,hden=2.0,dist=2300 is 37.750175678682254.
The interpolated lum value for T=1000000,hden=2.0,dist=2300 is 38.0.
The interpolated lum value for T=30000,hden=5.0,dist=2300 is 37.4995413685652.
The interpolated lum value for T=100000,hden=5.0,dist=2300 is 37.62081075906676.
The interpolated lum value for T=300000,hden=5.0,dist=2300 is 37.923631989384184.
The interpolated lum value for T=700000,hden=5.0,dist=2300 is 38.0.
The interpolated lum value for T=1000000,hden=5.0,dist=2300 is 38.0.

The interpolated lum value for T=30000,hden=0.75,dist=2500 is 36.0.
The interpolated lum value for T=100000,hden=0.75,dist=2500 is 36.04845787173087.
The interpolated lum value for T=300000,hden=0.75,dist=2500 is 36.52505677571444.
The interpolated lum value for T=700000,hden=0.75,dist=2500 is 37.17982965790094.
The interpolated lum value for T=1000000,hden=0.75,dist=2500 is 37.497916557201386.
The interpolated lum value for T=30000,hden=2.0,dist=2500 is 36.83065313719807.
The interpolated lum value for T=100000,hden=2.0,dist=2500 is 36.91712995716621.
The interpolated lum value for T=300000,hden=2.0,dist=2500 is 38.0.
The interpolated lum value for T=700000,hden=2.0,dist=2500 is 37.84637671816081.
The interpolated lum value for T=1000000,hden=2.0,dist=2500 is 38.0.
The interpolated lum value for T=30000,hden=5.0,dist=2500 is 37.635922416922035.
The interpolated lum value for T=100000,hden=5.0,dist=2500 is 37.744342120403395.
The interpolated lum value for T=300000,hden=5.0,dist=2500 is 38.0.
The interpolated lum value for T=700000,hden=5.0,dist=2500 is 38.0.
The interpolated lum value for T=1000000,hden=5.0,dist=2500 is 38.0.

The interpolated lum value for T=30000,hden=0.75,dist=2800 is 36.06751550496452.
The interpolated lum value for T=100000,hden=0.75,dist=2800 is 36.21566853046389.
The interpolated lum value for T=300000,hden=0.75,dist=2800 is 36.66754693541477.
The interpolated lum value for T=700000,hden=0.75,dist=2800 is 37.30919398300366.
The interpolated lum value for T=1000000,hden=0.75,dist=2800 is 37.625064367297185.
The interpolated lum value for T=30000,hden=2.0,dist=2800 is 36.95924661698511.
The interpolated lum value for T=100000,hden=2.0,dist=2800 is 37.054062348927616.
The interpolated lum value for T=300000,hden=2.0,dist=2800 is 37.42078560402868.
The interpolated lum value for T=700000,hden=2.0,dist=2800 is 37.9669825208715.
The interpolated lum value for T=1000000,hden=2.0,dist=2800 is 38.0.
The interpolated lum value for T=30000,hden=5.0,dist=2800 is 37.80215709535248.
The interpolated lum value for T=100000,hden=5.0,dist=2800 is 37.89217244862604.
The interpolated lum value for T=300000,hden=5.0,dist=2800 is 38.0.
The interpolated lum value for T=700000,hden=5.0,dist=2800 is 38.0.
The interpolated lum value for T=1000000,hden=5.0,dist=2800 is 38.0.
"""
