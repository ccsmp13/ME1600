# Greedy101Inc. 
# 10/27/24
# 
# Basketball Shot Analysis and Visualization
# 
# This script loads basketball shooting data from three different distances (15, 23, and 37 feet),
# fits quadratic polynomial trajectories to each set of data points, and calculates metrics
# such as release angles, maximum heights, and player heights for each shooting distance.
# It then plots the polynomial fits for each distance and displays the formatted results.


import numpy as np
import matplotlib.pyplot as plt
import Funcs as f
from numpy.polynomial import Polynomial as ply

# Load shooting data for distances of 15, 23, and 37 feet
fifteenFeet, twentythreeFeet, thirtysevenFeet = f.loadTexts()

# Fit polynomials for the 37 feet data
thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3 = f.fitPolys(thirtysevenFeet)

# Define x-values for plotting polynomials over respective distances
x15 = np.linspace(0, 15, 1000)
x23 = np.linspace(0, 23, 1000)
x37 = np.linspace(0, 37, 1000)

print("d   theta       player    y_max      phi")  # Header for displaying formatted results

# Process and plot data for the 15 feet shooting distance
fifteenPoly1, fifteenPoly2, fifteenPoly3 = f.fitPolys(fifteenFeet)
playerheight1, playerheight2, playerheight3 = f.playerh(fifteenFeet)
max1, max2, max3 = f.maxh(fifteenPoly1, fifteenPoly2, fifteenPoly3)
der1, der2, der3 = f.derivatives(fifteenPoly1, fifteenPoly2, fifteenPoly3)
releaseangle1, approachangle1, releaseangle2, approachangle2, releaseangle3, approachangle3 = f.angles(15, der1, der2, der3)
fifteenY1, fifteenY2, fifteenY3 = f.evalPoly(fifteenPoly1, fifteenPoly2, fifteenPoly3, x15)
plt.subplot(1, 3, 1)  # Set up first subplot
f.plotPoly(fifteenY1, fifteenY2, fifteenY3, x15, 15)

# Print formatted results for the 15 feet distance
f.printFormatted(15, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# Process and plot data for the 23 feet shooting distance
twentythreePoly1, twentythreePoly2, twentythreePoly3 = f.fitPolys(twentythreeFeet)
playerheight1, playerheight2, playerheight3 = f.playerh(twentythreeFeet)
max1, max2, max3 = f.maxh(twentythreePoly1, twentythreePoly2, twentythreePoly3)
der1, der2, der3 = f.derivatives(twentythreePoly1, twentythreePoly2, twentythreePoly3)
releaseangle1, approachangle1, releaseangle2, approachangle2, releaseangle3, approachangle3 = f.angles(23, der1, der2, der3)
twentythreeY1, twentythreeY2, twentythreeY3 = f.evalPoly(twentythreePoly1, twentythreePoly2, twentythreePoly3, x23)
plt.subplot(1, 3, 2)  # Set up second subplot
f.plotPoly(twentythreeY1, twentythreeY2, twentythreeY3, x23, 23)

# Print formatted results for the 23 feet distance
f.printFormatted(23, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# Process and plot data for the 37 feet shooting distance
thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3 = f.fitPolys(thirtysevenFeet)
playerheight1, playerheight2, playerheight3 = f.playerh(thirtysevenFeet)
max1, max2, max3 = f.maxh(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3)
der1, der2, der3 = f.derivatives(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3)
releaseangle1, approachangle1, releaseangle2, approachangle2, releaseangle3, approachangle3 = f.angles(37, der1, der2, der3)
thirtysevenY1, thirtysevenY2, thirtysevenY3 = f.evalPoly(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3, x37)
plt.subplot(1, 3, 3)  # Set up third subplot
f.plotPoly(thirtysevenY1, thirtysevenY2, thirtysevenY3, x37, 37)

# Print formatted results for the 37 feet distance
f.printFormatted(37, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# Display all subplots with polynomial trajectories for each distance
plt.show()