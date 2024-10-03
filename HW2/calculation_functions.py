import numpy as np
# Calculates the length of the R values and A values for the sphere and cube
def calc_length(v_internal, thickness):
    r = np.cbrt((.75 * v_internal) / np.pi)
    D = 2 * r
    A = np.cbrt(v_internal)
    D += (2 * thickness)
    A += (2 * thickness)
    return D, A
# Calculates the weight for the sphere and cube
def calc_weight(D, A, v_internal, tankDensity, liquidDensity):
    tank_A = (A ** 3) - v_internal
    tank_D = (4 / 3) * np.pi * (D / 2) ** 3 - v_internal
    tankWeight_A = tank_A * tankDensity
    tankWeight_D = tank_D * tankDensity
    liquidWeight_A = v_internal * liquidDensity
    liquidWeight_D = v_internal * liquidDensity
    totalWeight_A = (tankWeight_A + liquidWeight_A) * 9.81
    totalWeight_D = (tankWeight_D + liquidWeight_D) * 9.81
    
    return totalWeight_A, totalWeight_D

    