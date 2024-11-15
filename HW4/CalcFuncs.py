import numpy as np
import openpyxl
def TensileStress(diameter, force):
    # Calculates the tensile strength given diameter and force
    crossSectionArea = np.pi * (diameter / 2)**2
    return force / crossSectionArea

def unitConversion(pressure):
    # Converts USCS to ISO
    return pressure * .00689476

def gamma(F1, F2, F3, alpha, beta):
    # Calculates the gamma value
    alpha = np.radians(alpha)
    beta = np.radians(beta)
    gamma = np.arcsin((np.abs((F1*np.sin(alpha))+(F2*np.sin(beta))))/F3)
    gamma = np.degrees(gamma)
    return gamma

def boltForce(F1, F2, F3, alpha, beta, gamma):
    # Calculates the force of the bolt
    alpha = np.radians(alpha)
    beta = np.radians(beta)
    gamma = np.radians(gamma)
    boltForce = F1*np.cos(alpha)+F2*np.cos(beta)+F3*np.cos(gamma)
    return boltForce

