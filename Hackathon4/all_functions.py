import numpy as np
import openpyxl


def units_menu():
    '''
    This function allows the user to select the unit system they would like to 
    work in for this problem and returns it.
    '''
    print('********************************************************')
    print('              CONCRETE TROUGHS ANALYSIS                 ')
    print('********************************************************')
    print('Choose the unit system:')
    print('1. SI')
    print('2. USCS')
    print('********************************************************')
    # defines the unit system variable
    unitSystem = ''
    # Continues to ask the user for the number until they select a valid number
    while(len(unitSystem) == 0):
        unitSystemSelection = float(input('Select the unit system to use [1 or 2]: '))
        match unitSystemSelection:
            case 1:
                unitSystem = 'SI'
                lengthU, forceU, pressureU = 'm', 'N', 'MPa'
            case 2:
                unitSystem = 'USCS'
                lengthU, forceU, pressureU = 'in', 'lb', 'psi'
            case _:
                print('ERROR! Please select an appropriate option')
    return unitSystem, unitSystemSelection, lengthU, forceU, pressureU

def collect_data(unitSystem):
    '''
    This function opens the workbook and the appropriate sheet and extracts the data then returns it
    '''
    #Opens the workbook
    workbook = openpyxl.load_workbook("hack4.xlsx")

    # Selects the appropriate sheet
    sheetName = unitSystem + '_data'
    sheet = workbook[sheetName]

    # Extracts the data
    l = sheet["B2"].value
    t = sheet["B3"].value
    w = sheet["B4"].value
    d = sheet["B5"].value
    return l,t,w,d

def calculate_all(l, t, w, d, unitSystemSelection):
    '''
    This function performs the calculations required to find the missing values
    and returns them
    '''
    # Calculates theta
    theta = np.degrees(np.arccos(l / t))
    # Calculates force
    force = w / (2 * np.sin(np.radians(theta)))
    # If in SI converts m to mm
    if unitSystemSelection == 1:
        d *= 1000
    # Calculates sigma
    sigma = force / (np.pi * (d / 2) ** 2)
    # returns values
    return theta, force, sigma

def print_all(l,t,w,d,theta,f,sigma, lengthU, forceU, pressureU):
    '''
    This function prints the data for the user with appropriate units and 
    labels
    '''
    print('********************************************************')
    print('                          DATA                          ')
    print('********************************************************')
    print(f'L       ={l:8.2f} {lengthU}')
    print(f'T       ={t:8.2f} {lengthU}')
    print(f'W       ={w:8.2f} {forceU}')
    print(f'D       ={d:8.2f} {lengthU}\n')
    print('********************************************************')
    print('                         RESULTS                        ')
    print('********************************************************')
    print(f'Theta   ={theta:8.2f} degrees')
    print(f'F       ={f:8.2f} {forceU}')
    print(f'sigma   ={sigma:8.2f} {pressureU}')