import numpy as np
import matplotlib.pyplot as plt
import Funcs as f

# Load data from text files (no file prompting)
fifteenFeet, twentythreeFeet, thirtysevenFeet = f.loadTexts()

# Initialize x values for each distance
x15 = np.linspace(0, 15, 1000)
x23 = np.linspace(0, 23, 1000)
x37 = np.linspace(0, 37, 1000)

# Header for output
print("d   theta       player    y_max      phi")

# Process each dataset
for distance, data, x_vals in zip(
    [15, 23, 37],
    [fifteenFeet, twentythreeFeet, thirtysevenFeet],
    [x15, x23, x37]
):
    # Fit polynomials and perform calculations
    polys = f.fitPolys(data)
    player_heights = f.playerh(data)
    max_heights = f.maxh(polys)
    derivatives = f.derivatives(polys)
    angles = f.angles(distance, derivatives)
    y_vals = f.evalPoly(polys, x_vals)
    
    # Plot data and polynomials
    plt.subplot(1, 3, [15, 23, 37].index(distance) + 1)
    f.plotPoly(y_vals, x_vals)
    
    # Print formatted results
    f.printFormatted(distance, angles, player_heights, max_heights)

# Display plot
plt.show()
