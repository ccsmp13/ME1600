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
