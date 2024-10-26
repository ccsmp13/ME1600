import openpyxl
import matplotlib.pyplot as plt
import numpy as np


workbook = openpyxl.load_workbook("Example_workbook1.xlsx", data_only=True)
sheet1 = workbook["First_Sheet"]
sheet2 = workbook["Second_Sheet"]

columnX = sheet2["A1:A201"]
columnY = sheet2["B1:B201"]
values_X=[]
values_Y=[]
for each_rowX, each_rowY in zip(columnX,columnY): #for each row
    for each_cellX, each_cellY in zip(each_rowX,each_rowY): #for each cell in each row
        values_X.append(each_cellY.value)
        values_Y.append(each_cellX.value)
        
   
    
xlabel = values_X.pop(0)
ylabel = values_Y.pop(0) 

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.plot(values_X,values_Y)

plt.show()