import math
import time
from terminalCLS import cls
import input_functions as inpt
import calculation_functions as calc
import output_functions as outpt

cls()

firstName, lastName = inpt.name()

outpt.welcomeMessage(firstName,lastName)

units = inpt.units(firstName)

r = inpt.radius(firstName,units)

outpt.echoValues(firstName,r,units)

print('Calculating the area and the circumference now...')

time.sleep(2)

area = calc.CalcArea(r)
circumference = calc.CalcCircumference(r)

outpt.finalMessage(firstName,lastName,units,r,area,circumference)