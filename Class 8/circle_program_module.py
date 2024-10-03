import math
import time
from terminalCLS import cls
import input_functions as inpt
import calculation_functions as calc
import output_functions as outpt
import numpy as np
import matplotlib.pyplot as plt

cls()

firstName, lastName = inpt.name()

outpt.welcomeMessage(firstName,lastName)

units = inpt.units(firstName)

minRad,maxRad = inpt.rangeStepRadius(firstName,units)


outpt.echoValues(firstName,minRad,maxRad,units)

radVector = np.linspace(minRad, maxRad, 100)
print('Calculating the area and the circumference now...')

time.sleep(2)

areaVector = calc.CalcArea(radVector)
circumferenceVector = calc.CalcCircumference(radVector)


# Using the figure function for opening a figure that will contain two plots
figure_circle=plt.figure(5)
# Using the plot function, plotting both y and z in the same figure
plt.plot(radVector,areaVector, "m:")
plt.plot(radVector,circumferenceVector, "k--")
# Adding the labels and title and legends
xlabel_string="Radius [{}]"
alabel_string="Area [{}^2]"
clabel_string="Circumference [{}]"
ylabel_string="Area [{}^2] and Circumference [{}]"
title_string="Area and Circumference of a circle of radius {:.2f}:{:.2f} {}"
plt.xlabel(xlabel_string.format(units))
plt.ylabel(ylabel_string.format(units,units))
plt.title(title_string.format(minRad,maxRad,units))
plt.legend([alabel_string.format(units),clabel_string.format(units)])
# Save this figure
figure_circle.savefig("figure_circle.png", dpi=600)
# Showing the plot
plt.show()


# outpt.finalMessage(firstName,lastName,units,radVector,areaVector,circumferenceVector)