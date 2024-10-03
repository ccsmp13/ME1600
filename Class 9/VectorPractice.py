import numpy as np
from terminalCLS import cls

cls()

u=np.array([1.2, 3.4, 5.6])
v=np.array([2.3, 5.8, 19.2])
print("\nThe vector v:")
print(v)
magV=np.linalg.norm(v)
print("\nThe magnitude of v:")
print(magV)

print("\nThe vector u:")
print(u)
magU=np.linalg.norm(u)
print("\nThe magnitude of u:")
print(magU)

elementProduct = u * v

dotProduct = np.dot(u,v)

crossProduct = np.cross(u,v)

print("\nThe element product:")
print(elementProduct)

print("\nThe dot product:")
print(dotProduct)

print("\nThe cross product:")
print(crossProduct)

# This is a test of git