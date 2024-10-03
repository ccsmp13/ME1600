import numpy as np

# Get user input for min value, max value, tank thickness, tank density, and liquid density then returns them
def ask_user():
    minVal = float(input("Please enter the minimum value of V_internal in m^3: "))
    maxVal = float(input("Please enter the maximum value of V_internal in m^3: "))
    tankThickness = float(input("Please enter the tank thickness in m: "))
    tankDensity = float(input("Please enter the density of the tank material in kg/m^3: "))
    liquidDensity = float(input("Please enter the density of the liquid in kg/m^3: "))
    v_internalRange = np.linspace(minVal, maxVal, 1000)
    print("+++++++++++++++++++++++++++++++++++++")
    
    return v_internalRange, tankThickness, tankDensity, liquidDensity, minVal, maxVal
