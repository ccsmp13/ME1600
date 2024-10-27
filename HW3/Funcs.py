# import numpy as np
# from numpy.polynomial import Polynomial as ply
# import matplotlib.pyplot as plt
# import Funcs as f
# def loadTexts():
#     fifteenFeet = np.loadtxt('shootdata15.txt', delimiter = '\t')
#     twentythreeFeet = np.loadtxt('shootdata23.txt', delimiter = '\t')
#     thirtysevenFeet = np.loadtxt('shootdata37.txt', delimiter = '\t') 
#     return fifteenFeet, twentythreeFeet, thirtysevenFeet

# def fitPolys(poly):
#     poly1 = ply.fit(poly[0,:],poly[1,:],2)
#     poly2 = ply.fit(poly[2,:],poly[3,:],2)
#     poly3 = ply.fit(poly[4,:],poly[5,:],2)
#     return poly1, poly2, poly3

# def evalPoly(poly1, poly2, poly3, x):
#     y1 = poly1(x)
#     y2 = poly2(x)
#     y3 = poly3(x)
#     return y1, y2, y3

# def plotPoly(y1,y2,y3,x):
#     plt.plot(x,y1)
#     plt.plot(x,y2)
#     plt.plot(x,y3)
    
#     plt.ylim([0,40])
#     plt.xlim([0,40])

# def plotPoints(x,y):
#     plt.plot(x,y,"r")

# def playerh(dataset):
#     initialheight1 = dataset[1,0]
#     initialheight2 = dataset[3,0]
#     initialheight3 = dataset[5,0]
#     playerheight1 = initialheight1 / 1.2
#     playerheight2 = initialheight2 / 1.2
#     playerheight3 = initialheight3 / 1.2
#     return playerheight1, playerheight2, playerheight3

# def maxh(polynomial1,polynomial2,polynomial3):
#     fp1_der = ply.deriv(polynomial1)
#     fp2_der = ply.deriv(polynomial2)
#     fp3_der = ply.deriv(polynomial3)
#     max1 = ply.roots(fp1_der)
#     max2 = ply.roots(fp2_der)
#     max3 = ply.roots(fp3_der)
    
#     return polynomial1(max1[0]), polynomial2(max2[0]), polynomial3(max3[0])

# def angles(endPoint,der1,der2,der3):
#     der1zero = der1(0)
#     der2zero = der2(0)
#     der3zero = der3(0)
#     der1end = der1(endPoint)
#     der2end = der2(endPoint)
#     der3end = der3(endPoint)
#     releaseangle_rad1 = np.arctan(der1zero)
#     approachangle_rad1 = np.arctan(der1end)*(-1)
    
#     releaseangle_deg1 = np.degrees(releaseangle_rad1)
#     approachangle_deg1 = np.degrees(approachangle_rad1)

#     releaseangle_rad2 = np.arctan(der2zero)
#     approachangle_rad2 = np.arctan(der2end)*(-1)
    
#     releaseangle_deg2 = np.degrees(releaseangle_rad2)
#     approachangle_deg2 = np.degrees(approachangle_rad2)

#     releaseangle_rad3 = np.arctan(der3zero)
#     approachangle_rad3 = np.arctan(der3end)*(-1)
    
#     releaseangle_deg3 = np.degrees(releaseangle_rad3)
#     approachangle_deg3 = np.degrees(approachangle_rad3)
#     return releaseangle_deg1,approachangle_deg1,releaseangle_deg2,approachangle_deg2,releaseangle_deg3,approachangle_deg3

# def derivatives(polynomial1 ,polynomial2, polynomial3):
#     der1 = ply.deriv(polynomial1)
#     der2 = ply.deriv(polynomial2)
#     der3 = ply.deriv(polynomial3)
#     return der1, der2, der3

# def derivAt(poly, at):
#     deriv = ply.deriv(poly)
#     return deriv(at)


# def printFormatted(feet, theta1, theta2, theta3, playerheight1, playerheight2, playerheight3, max1, max2, max3, phi1, phi2, phi3):
#     print(f"{feet}  {theta1:.2f}(deg)  {playerheight1:.2f}(ft)  {max1:.2f}(ft)  {phi1:.2f}(deg)")
#     print(f"{feet}  {theta2:.2f}(deg)  {playerheight2:.2f}(ft)  {max2:.2f}(ft)  {phi2:.2f}(deg)")
#     print(f"{feet}  {theta3:.2f}(deg)  {playerheight3:.2f}(ft)  {max3:.2f}(ft)  {phi3:.2f}(deg)")

import numpy as np
from numpy.polynomial import Polynomial as ply
import matplotlib.pyplot as plt

def loadTexts():
    filenames = ['shootdata15.txt', 'shootdata23.txt', 'shootdata37.txt']
    data = [np.loadtxt(fname, delimiter='\t') for fname in filenames]
    return data

def fitPolys(data):
    return [ply.fit(data[i, :], data[i + 1, :], 2) for i in range(0, data.shape[0], 2)]

def evalPoly(polys, x):
    return [poly(x) for poly in polys]

def plotPoly(y_vals, x):
    for y in y_vals:
        plt.plot(x, y)
    plt.ylim([0, 40])
    plt.xlim([0, 40])

def playerh(data):
    return [data[i, 0] / 1.2 for i in range(1, data.shape[0], 2)]

def maxh(polys):
    return [poly(ply.roots(ply.deriv(poly))[0]) for poly in polys]

def angles(end_point, derivatives):
    angles = []
    for der in derivatives:
        release_angle = np.degrees(np.arctan(der(0)))
        approach_angle = -np.degrees(np.arctan(der(end_point)))
        angles.append((release_angle, approach_angle))
    return angles

def derivatives(polys):
    return [ply.deriv(poly) for poly in polys]

def derivAt(poly, at):
    return ply.deriv(poly)(at)

def printFormatted(feet, angles, player_heights, max_heights):
    for i in range(len(angles)):
        release, approach = angles[i]
        print(f"{feet}  {release:.2f}(deg)  {player_heights[i]:.2f}(ft)  {max_heights[i]:.2f}(ft)  {approach:.2f}(deg)")
