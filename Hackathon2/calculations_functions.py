import numpy as np

# Function to calculate the base area of a pyramid (square base)
def Base(side):
    return side ** 2  

# Function to calculate the surface area of a pyramid
def SurfaceArea(side, slant):
    return ((side * slant) / 2) * 4 + side ** 2 

# Function to calculate the height of the pyramid
def Height(side, slant):
    return np.sqrt(slant ** 2 - (side / 2) ** 2)  # Return the height

# Function to calculate the volume of a pyramid
def Volume(base, height):
    return (base * height) / 3 