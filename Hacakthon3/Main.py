# Collin Sampson
# 10/28/24
# 
# Hackathon 3
# 
# This is code that visualizes the path ofthe trajectory of a projectile
# that was used as a murder weapon to aid a team of forensic engineers
import numpy as np
from numpy.polynomial import Polynomial as ply
import matplotlib.pyplot as plt
from terminalCLS import cls

# Clear the terminall
cls()

# Load experimental data from a text file 'exp_averages.txt'
txtData = np.loadtxt('exp_averages.txt')

# Separate the loaded data into x and y values
xVals = txtData[:,0]
yVals = txtData[:,1]

# Fit a second-order polynomial (quadratic) to the experimental data
fittedPoly = ply.fit(xVals, yVals, 2)

# Find the roots (x-intercepts) of the fitted polynomial
roots = fittedPoly.roots()
landingPoint = roots[1]  # Assumes the second root is the landing point of the projectile

# Estimate the height of the suspect as 90% of the y-intercept (height at x=0)
suspectHeight = fittedPoly(0) / 0.9

# Calculate the derivative of the fitted polynomial, representing the slope of the tangent
derivPoly = fittedPoly.deriv()

# Calculate the launch angle in degrees using the tangent of the slope at x=0
launchAngle = np.degrees(np.arctan(derivPoly(0)))

# Find the x-value where the maximum height occurs (i.e., root of the derivative)
xOfMax = derivPoly.roots()

# Calculate the maximum height by evaluating the fitted polynomial at the maximum x-value
maxHeight = fittedPoly(xOfMax)

# Generate a range of x values for plotting the fitted polynomial
x = np.linspace(0, 12, 1000)

# Prepare the interactive message for user selection
reply = True
message =  "*********************************************\n"
message += "          Forensic Engineering 101             \n"
message += "*********************************************\n"
message += "1. Experimental data points\n"
message += "2. Second order polynomial data fit\n"
message += "3. Tangent at x=0\n"
message += "4. Projectile maximum elevation\n"
message += "*********************************************\n"
message += "5. SHOW THE PLOT AND EXIT\n"
message += "*********************************************\n"

# Interactive loop for plotting based on user selection
while(reply):
    # Display message and prompt user for input
    selection = float(input(message))
        
    # Perform action based on user selection
    match selection:
        case 1:
            # Plot experimental data points as red dots
            plt.plot(xVals, yVals, "r.")
            
        case 2:
            # Plot the fitted polynomial as a blue curve
            plt.plot(x, fittedPoly(x), 'b')

        case 3:
            # Plot the tangent line at x=0 as a dashed cyan line
            xTan = np.linspace(0, 3, 300)
            plt.plot(xTan, derivPoly(0) * xTan + fittedPoly(0), 'c--')
            
        case 4:
            # Plot the maximum height point as a black star
            plt.plot(xOfMax, maxHeight, 'k*')
            
        case 5:
            # Exit the loop, show the plot, and display additional information
            reply = False
            plt.xlim(0)
            plt.ylim(0)
            # Create a title with launch angle, suspect height, landing point, and max height
            message = f'Launch Angle: {launchAngle:.0f} degrees\n'
            message += f'Suspect height: {suspectHeight:.2f} meters\n'
            message += f'Landing point: {landingPoint:.2f} meters\n'
            message += f'Max elevation: {maxHeight[0]:.3f} meters'
            plt.title(message)
            plt.xlabel('horizontal coordinate (m)')
            plt.ylabel('vertical coordinate (m)')
            plt.tight_layout()
            plt.show()
            
        case _:
            # Handle invalid input selection
            print("Error! Your selection is invalid.")
