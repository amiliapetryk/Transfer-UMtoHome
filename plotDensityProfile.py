# import packages
import matplotlib.pyplot as plt
import numpy as np

# set initial conditions
depth = list()
hden = list()
radius = list()

rad = 12

# open file, read lines, and append to appropriate list
file = open("../cloudyCode/singleBBDenTableTest.ovr","r")

for line in file:
    # get rid of the first line and grid delineating lines
    if line[0].isnumeric():
        num = line.split("\t")
        depth.append(num[0])
        hden.append(float(num[3]))
    
# make depth (distance from illuminating face) into radius (distance from geometric center)
for num in depth:
    radius.append((float(num)+float(10**rad))/(3.086e+18))


# make into arrays
radiusArray = np.array(radius)
hdenArray = np.array(hden)

# Ionization Fraction over Depth, (insert whatever realistic spectra is here), L=5000 solar

# create graph
plt.scatter(radiusArray,hdenArray)
plt.title("Density profile of single BB T=300,000 L=36")
plt.xlabel("Radius [parsec]")
plt.ylabel("Density [cm-3]")
plt.show()
