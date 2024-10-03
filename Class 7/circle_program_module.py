import math
import time
from terminalCLS import cls
import input_functions as inpt
import calculation_functions as calc
import output_functions as outpt
import numpy as np

cls()

firstName, lastName = inpt.name()

outpt.welcomeMessage(firstName,lastName)

units = inpt.units(firstName)

minRad,maxRad,stepSize = inpt.rangeStepRadius(firstName,units)


outpt.echoValues(firstName,minRad,maxRad,stepSize,units)

radVector = np.arange(minRad, maxRad, stepSize)
print('Calculating the area and the circumference now...')

time.sleep(2)

areaVector = calc.CalcArea(radVector)
circumferenceVector = calc.CalcCircumference(radVector)

outpt.finalMessage(firstName,lastName,units,radVector,areaVector,circumferenceVector)