from numpy.polynomial import Polynomial as ply
import numpy as np
import matplotlib.pyplot as plt


snowMatrix = np.loadtxt("snow.txt")

weeks = snowMatrix[1,:]
snow = snowMatrix[0,:]

plt.plot(weeks,snow,"*b")

snowfallFit = ply.fit(weeks,snow,2)
snowfallRoots = ply.roots(snowfallFit)
x = np.linspace(snowfallRoots[0],snowfallRoots[1],1000)
y = snowfallFit(x)
weekPred = np.ceil(snowfallRoots[1])
plt.ylim([0,100])
plt.xlim([0,weekPred])
plt.plot(x,y,"--c")

plt.title("The snow will be gone at week {}".format(weekPred))
plt.xlabel('Weeks')
plt.ylabel('Snow depth in inches')
plt.show()
