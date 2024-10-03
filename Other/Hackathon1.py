# Find the viscosity for different engine oils

# Collin Sampson
# 09/16/24
import math

# Declare different scenarios
d = .00098
Rf = 912
t = 9.12

# d = .00112
# Rf = 947
# t = 14.2

# d = .00102
# Rf = 998
# t = 8.7


# Declare constants
g = 9.81
displacement = .1
Rs = 7830

# Calculate radius
radius = d / 2
# Calculate Volume
volume = (4 * math.pi * radius ** 3) / 3
# Calculate mass
mass = Rs * volume
# Calculate weight
weight = mass * g
# Calculate buoyent force
Fb = Rf * g * volume
# Calculate drag
Fd = weight - Fb
# Calculate area
area = math.pi * d ** 2 / 4
# Calculate Velocity
velo = displacement / t
# Calculate drag coefficient
Cd = (2 * Fd) / (Rf * area * velo ** 2)
# Calculate Rhenolds number
Re = 24 / Cd
# Calculate Viscosity
mu = Rf * velo * d / Re
# Print Results
print(mu)