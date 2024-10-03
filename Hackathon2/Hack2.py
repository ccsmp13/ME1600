# This program calculates the 
# height, volume, area of base and surface area

# 10/2/24
# Collin Sampson

import calculations_functions as calc
import input_functions as inpt
import output_functions as out
from terminalCLS import cls

cls()

# calling functions that ask the user for inputs
units = inpt.ask_units()
slant, side = inpt.ask_lengths(units)

# Calculate bse, surface area, height and volume of the pyramid
base = calc.Base(side)
surfaceArea = calc.SurfaceArea(side, slant)
height = calc.Height(side, slant)
volume = calc.Volume(base, height)

# Print out the data calculated to the terminal
out.PrintData(side, slant,units)
out.PrintResults(base, surfaceArea, height, volume, units)