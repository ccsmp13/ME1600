#ME 1600
#Homework 4
#Greedy 101 Inc.
# This code calculates the forces exerted on a bolt and the gamma value
# given values from an excel file

#imports programs/modules
import openpyxl
import CalcFuncs as calc

#Prints the option between ISO and USCS units
print('**********************************************')
print('           BOLT AND CABLES STRESSED           ')
print('**********************************************')
print('Choose the unit system:')
print('1. ISO')
print('2. USCS')
print('**********************************************')

#Initizialize loop variables
unitSystemSelection = 0
unitSystem = ''

#Asks user for unit system
while(len(unitSystem) == 0):
    
    unitSystemSelection = float(input('Select the unit system to use [1 or 2]: '))
    match unitSystemSelection:
        case 1:
            unitSystem = 'ISO'
            reply = False
        case 2:
            unitSystem = 'USCS'
            reply = False
        case _:
            print('ERROR! Please select an appropriate option')

#Opens the workbook
workbook = openpyxl.load_workbook("data.xlsx")

# Selects the appropriate sheet
sheetName = unitSystem + '_data'
sheet = workbook[sheetName]

# Captures the data from the appropriate sheet
data = sheet["C3:C9"]
data_names = sheet["B3:B9"]

#Checks the data for negatives and prompts the user to input positive
print("\n**********************************************")
print("       CHECKING THE ORIGINAL DATA FILE        ")
print("**********************************************\n")
i = 3
for each_rowA, each_rowB in zip(data_names,data): 
    for each_cellA, each_cellB in zip(each_rowA,each_rowB):
        while(each_cellB.value < 0):
            sheet.cell(i,3,float(input(each_cellA.value + ' is negative. Please insert it again: ')))            
        i += 1
workbook.save('data.xlsx')
print('All data are positive.')

#asigns names to cell values        
F1 = sheet["C3"].value
F2 = sheet["C4"].value
F3 = sheet["C5"].value
alpha = sheet["C6"].value
beta = sheet["C7"].value
cableD = sheet["C8"].value
boltD = sheet["C9"].value

N_TO_LB = 0.224808943
CM_TO_IN = 0.39370079
#filters from the choice of units into the corrisponding labels, and sets values 
# to USCS no matter the user selection to simplify the calculation process
if unitSystemSelection == 1:
    force = "N"
    length = "cm"
    F1uscs, F2uscs, F3uscs = F1 * N_TO_LB, F2 * N_TO_LB, F3 * N_TO_LB #Convert newtons to lbs
    cableDuscs, boltDuscs = cableD * CM_TO_IN, boltD * CM_TO_IN #Convert cm to in
else:
    force = "lbs"
    length = "in"
    F1uscs, F2uscs, F3uscs = F1, F2, F3
    cableDuscs, boltDuscs = cableD, boltD

#prints data with units
print("\n**********************************************")
print("                    DATA                      ")
print("**********************************************")
print(f"F1      ={F1:10.2f} {force}")
print(f"F2      ={F2:10.2f} {force}") 
print(f"F3      ={F3:10.2f} {force}")
print(f"alpha   ={alpha:10.2f} degrees")
print(f"beta    ={beta:10.2f} degrees")
print(f"cable D ={cableD:10.2f} {length}")
print(f"bolt D  ={boltD:10.2f} {length}")

#calculates the gamma and sigma values in USCS
gamma = calc.gamma(F1uscs, F2uscs, F3uscs, alpha, beta)
boltForce = calc.boltForce(F1uscs, F2uscs, F3uscs, alpha, beta, gamma)
sigma1USCS = calc.TensileStress(cableDuscs,F1uscs)
sigma2USCS = calc.TensileStress(cableDuscs,F2uscs)
sigma3USCS = calc.TensileStress(cableDuscs,F3uscs)
sigma4USCS = calc.TensileStress(boltDuscs, boltForce)

#converts the units to ISO
sigma1ISO = calc.unitConversion(sigma1USCS)
sigma2ISO = calc.unitConversion(sigma2USCS)
sigma3ISO = calc.unitConversion(sigma3USCS)
sigma4ISO = calc.unitConversion(sigma4USCS)

#prints the final results
print('********************************************************')
print('                       RESULTS                          ')
print('********************************************************')
print(f'gamma  = {gamma:10.2f} degrees')
print(f'sigma1 = {sigma1ISO:10.2f} MPa,{sigma1USCS:10.2f} psi')
print(f'sigma2 = {sigma2ISO:10.2f} MPa,{sigma2USCS:10.2f} psi')
print(f'sigma3 = {sigma3ISO:10.2f} MPa,{sigma3USCS:10.2f} psi')
print(f'sigma4 = {sigma4ISO:10.2f} MPa,{sigma4USCS:10.2f} psi')
