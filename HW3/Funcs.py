# Greedy101Inc. 
# 10/27/24
# 
# 
# This script loads basketball shooting data from three different distances (15, 23, and 37 feet),
# fits quadratic polynomial trajectories to each set of data points, and calculates metrics
# such as release angles, maximum heights, and player heights for each shooting distance.
# It then plots the polynomial fits for each distance and displays the formatted results.
import numpy as np
from numpy.polynomial import Polynomial as ply
import matplotlib.pyplot as plt
import Funcs as f

# Load shooting data from text files, delimited by tabs
def loadTexts():
    fifteenFeet = np.loadtxt('shootdata15.txt', delimiter='\t')
    twentythreeFeet = np.loadtxt('shootdata23.txt', delimiter='\t')
    thirtysevenFeet = np.loadtxt('shootdata37.txt', delimiter='\t')
    return fifteenFeet, twentythreeFeet, thirtysevenFeet

# Fit quadratic polynomials to data points for different shooting distances
def fitPolys(poly):
    poly1 = ply.fit(poly[0, :], poly[1, :], 2)
    poly2 = ply.fit(poly[2, :], poly[3, :], 2)
    poly3 = ply.fit(poly[4, :], poly[5, :], 2)
    return poly1, poly2, poly3

# Evaluate the polynomial trajectories at specified x-values
def evalPoly(poly1, poly2, poly3, x):
    y1 = poly1(x)
    y2 = poly2(x)
    y3 = poly3(x)
    return y1, y2, y3

# Plot polynomial trajectories with labels and title
def plotPoly(y1, y2, y3, x, case):
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Data and fitting for d=" + str(case))
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.ylim([0, 40])
    plt.xlim([0, 40])

# Plot data points with a red marker
def plotPoints(x, y):
    plt.plot(x, y, "r")

# Calculate estimated player height based on the initial height of shots
def playerh(dataset):
    initialheight1 = dataset[1, 0]
    initialheight2 = dataset[3, 0]
    initialheight3 = dataset[5, 0]
    playerheight1 = initialheight1 / 1.2
    playerheight2 = initialheight2 / 1.2
    playerheight3 = initialheight3 / 1.2
    return playerheight1, playerheight2, playerheight3

# Find the maximum height of each polynomial trajectory
def maxh(polynomial1, polynomial2, polynomial3):
    fp1_der = ply.deriv(polynomial1)
    fp2_der = ply.deriv(polynomial2)
    fp3_der = ply.deriv(polynomial3)
    max1 = ply.roots(fp1_der)
    max2 = ply.roots(fp2_der)
    max3 = ply.roots(fp3_der)
    return polynomial1(max1[0]), polynomial2(max2[0]), polynomial3(max3[0])

# Calculate release and approach angles based on polynomial derivatives
def angles(endPoint, der1, der2, der3):
    der1zero = der1(0)
    der2zero = der2(0)
    der3zero = der3(0)
    der1end = der1(endPoint)
    der2end = der2(endPoint)
    der3end = der3(endPoint)
    releaseangle_rad1 = np.arctan(der1zero)
    approachangle_rad1 = np.arctan(der1end) * (-1)
    releaseangle_deg1 = np.degrees(releaseangle_rad1)
    approachangle_deg1 = np.degrees(approachangle_rad1)
    releaseangle_rad2 = np.arctan(der2zero)
    approachangle_rad2 = np.arctan(der2end) * (-1)
    releaseangle_deg2 = np.degrees(releaseangle_rad2)
    approachangle_deg2 = np.degrees(approachangle_rad2)
    releaseangle_rad3 = np.arctan(der3zero)
    approachangle_rad3 = np.arctan(der3end) * (-1)
    releaseangle_deg3 = np.degrees(releaseangle_rad3)
    approachangle_deg3 = np.degrees(approachangle_rad3)
    return releaseangle_deg1, approachangle_deg1, releaseangle_deg2, approachangle_deg2, releaseangle_deg3, approachangle_deg3

# Calculate the first derivative of each polynomial
def derivatives(polynomial1, polynomial2, polynomial3):
    der1 = ply.deriv(polynomial1)
    der2 = ply.deriv(polynomial2)
    der3 = ply.deriv(polynomial3)
    return der1, der2, der3

# Evaluate the derivative of a polynomial at a specific point
def derivAt(poly, at):
    deriv = ply.deriv(poly)
    return deriv(at)

# Print formatted results including angles, heights, and distances
def printFormatted(feet, theta1, theta2, theta3, playerheight1, playerheight2, playerheight3, max1, max2, max3, phi1, phi2, phi3):
    print(f"{feet}  {theta1:.2f}(deg)  {playerheight1:.2f}(ft)  {max1:.2f}(ft)  {phi1:.2f}(deg)")
    print(f"{feet}  {theta2:.2f}(deg)  {playerheight2:.2f}(ft)  {max2:.2f}(ft)  {phi2:.2f}(deg)")
    print(f"{feet}  {theta3:.2f}(deg)  {playerheight3:.2f}(ft)  {max3:.2f}(ft)  {phi3:.2f}(deg)")