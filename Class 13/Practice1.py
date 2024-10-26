import numpy as np
import matplotlib.pyplot as plt
csvPractice1 = np.loadtxt('practice1.csv', delimiter= ',', skiprows= 1 )

col1 = csvPractice1[:,0]
col2 = csvPractice1[:,1]
col3 = csvPractice1[:,2]
col4 = csvPractice1[:,3]
col5 = csvPractice1[:,4]
col6 = csvPractice1[:,5]
col7 = csvPractice1[:,6]
col8 = csvPractice1[:,7]

plt.plot(col1,col2,'y')
plt.plot(col3,col4,'k')
plt.plot(col5,col6,'k')
plt.plot(col7,col8,'r')

plt.axis('equal')
plt.show()