# Collin Sampson
# 11/13/24
# 
# Program for calculating the angle theta, tensile stress and tensioon in a system
# of concrete beams
import all_functions as func
from terminalCLS import cls

cls()


unitSystem, unitSystemSelection, lengthU, forceU, pressureU = func.units_menu()

l, t, w, d = func.collect_data(unitSystem)

theta, force, sigma = func.calculate_all(l, t, w, d, unitSystemSelection)

func.print_all(l, t, w, d, theta, force, sigma, lengthU, forceU, pressureU)

