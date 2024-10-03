# Find and plot the side length, diameter and weight of 
# spherical tanks and cubical tanks
# 
# 9/30/24
# Collin Sampson
import input_functions as inpt
import calculation_functions as calc
import output_functions as out
from terminalCLS import cls

# Clears the console
cls()
# Gets input from user
v_internal, tankThickness, tankDensity, liquidDensity, minVal, maxVal = inpt.ask_user()
# Calculates the length for side A and diameter D
D, A = calc.calc_length(v_internal, tankThickness)
# Calculates weight of spehere and cube including liquid
weight_A, weight_D = calc.calc_weight(D, A, v_internal, tankDensity, liquidDensity)
# Prints out a graphical interpretation and in the terminal
out.print_data(minVal, maxVal, tankThickness, tankDensity, liquidDensity)
out.plot_length_weight(v_internal, D, A, weight_A, weight_D)
