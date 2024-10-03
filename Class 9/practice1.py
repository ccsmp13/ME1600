import numpy as np
myMatrix=np.array([[3,4],[7,9],[35,100]])


r, c = np.shape(myMatrix)

myMatrix[r - 1, c - 1] = 27

print(myMatrix)