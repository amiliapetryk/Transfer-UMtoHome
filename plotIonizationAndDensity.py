# the goal of this script is to plot the ovr output from BB.in

# import packages
import matplotlib.pyplot as plt
import numpy as np

# set initial conditions
depth = list()
radius = list()
hden = list()
hi = list()
hii = list()
hfrac = list()

innerRad = 13
h=0.75
dist=2300
#singleBBDenTableTest_L38_r13_stopRad_h5.0_d2300_iterateUntilConvergence.ovr
filename = "singleBBDenTableTest_L38_r13_stopRad_h"+str(h)+"_d"+str(dist)+".ovr"

# set radii
if dist == 2300:
	rad = 13.200260477310094
if dist == 2500:
	rad = 14.348109214467494
if dist == 2800:
	rad = 16.069882320203593

# open file, read lines, and append to appropriate list
ovr = open("../cloudyCode/"+filename,"r")

for line in ovr:
    # get rid of the first line and grid delineating lines
    if line[0].isnumeric():
        num = line.split("\t")
        depth.append(num[0])
        hden.append(float(num[3]))
        hi.append(num[6])
        hii.append(num[7])

# make ionization fraction
for num in range(0,int(len(depth))):
    frac = float(hii[num])/(float(hii[num])+float(hi[num]))
    hfrac.append(frac)
    
# make depth (distance from illuminating face) into radius (distance from geometric center)
for num in depth:
    radius.append((float(num)+float(10**innerRad))/(3.086e+18)) # this is just the depth converted into pc its not a radius

# make into arrays
hdenArray = np.array(hden)
ionArray = np.array(hfrac)
radiusArray = np.array(radius)

# normalize the hden array (so on same scale of 0-1 as ionization array)
normalHdenArray = np.divide(hdenArray,h)

fig, ax1 = plt.subplots()
plt.title("Ionization fraction and hden vs. radius for T=300,000, L=38, hden={}, d={} and dlaw table".format(h,dist))
plt.xlabel("Radius [parsec]")
plt.ylabel("Ionization Fraction (HII/(HI + HII))",color="slateblue")
plt.legend()

ax2 = ax1.twinx()
ax2.scatter(radiusArray,ionArray,color="slateblue",s=8,label="BB output")
ax2.scatter(radiusArray,normalHdenArray,color="seagreen",s=8,label="hden profile")
plt.ylabel("Normalized density [cm-3]",color="seagreen")
plt.vlines(rad,0,1,linestyle="dashed",color="deepskyblue",label="Shock front = {:2f} pc".format(rad))
plt.legend()
plt.show()

"""
# create graph
plt.scatter(radiusArray,ionArray,color="slateblue",s=8,label="BB output")
plt.scatter(radiusArray,hdenArray,color="seagreen",s=8,label="hden profile")
plt.title("Ionization fraction and hden vs. radius for T=300,000, L=38, hden={}, d={} and dlaw table".format(h,dist))
plt.xlabel("Radius [parsec]")
plt.ylabel("Ionization Fraction (HII/(HI + HII))",color="slateblue")
plt.vlines(rad,hfrac[0],hfrac[-1],linestyle="dashed",color="deepskyblue",label="Shock front = {:2f} pc".format(rad))
plt.legend()
plt.show()

##############################################################################################################################


# create graph
plt.scatter(radiusArray,hdenArray,color="slateblue",s=8,label="hden profile")
plt.title("Density profile of single BB T=300,000 L=38, hden={}, d={} and dlaw table".format(h,dist))
plt.xlabel("Radius [parsec]")
plt.ylabel("Density [cm-3]")
plt.vlines(rad,hden[0],hden[-1],linestyle="dashed",color="deepskyblue",label="Shock front = {:2f} pc".format(rad))
plt.legend()
plt.show()
"""
