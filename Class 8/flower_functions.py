import numpy as np
import matplotlib.pyplot as plt



def CreateVars():
    theta = np.linspace(0,2 * np.pi, 1000)
    RofTheta = np.sin(4 * theta) * np.cos(4 * theta)
    return RofTheta, theta

def PlotFlower(func, theta):
    
    plt.polar(theta, func, "m--")
    plt.title("Polar R(theta)")
    plt.show()