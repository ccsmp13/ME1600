# import numpy as np
# import matplotlib.pyplot as plt
# import Funcs as f
# from numpy.polynomial import Polynomial as ply

# fifteenFeet, twentythreeFeet, thirtysevenFeet = f.loadTexts()

# thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3 = f.fitPolys(thirtysevenFeet)

# x15 = np.linspace(0,15,1000)
# x23 = np.linspace(0,23,1000)
# x37 = np.linspace(0,37,1000)

# print("d   theta       player    y_max      phi")

# fifteenPoly1, fifteenPoly2, fifteenPoly3 = f.fitPolys(fifteenFeet)
# playerheight1, playerheight2, playerheight3= f.playerh(fifteenFeet)
# max1, max2, max3 = f.maxh(fifteenPoly1, fifteenPoly2, fifteenPoly3)
# der1, der2, der3 = f.derivatives(fifteenPoly1, fifteenPoly2, fifteenPoly3)
# releaseangle1,approachangle1,releaseangle2,approachangle2,releaseangle3,approachangle3=f.angles(15,der1,der2,der3)
# fifteenY1, fifteenY2, fifteenY3 = f.evalPoly(fifteenPoly1, fifteenPoly2, fifteenPoly3, x15)
# plt.subplot(1,3,1)
# f.plotPoly(fifteenY1, fifteenY2, fifteenY3, x15)

# f.printFormatted(15, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# twentythreePoly1, twentythreePoly2, twentythreePoly3 = f.fitPolys(twentythreeFeet)
# playerheight1, playerheight2, playerheight3= f.playerh(twentythreeFeet)
# max1, max2, max3 = f.maxh(twentythreePoly1, twentythreePoly2, twentythreePoly3)
# der1, der2, der3 = f.derivatives(twentythreePoly1, twentythreePoly2, twentythreePoly3)
# releaseangle1,approachangle1,releaseangle2,approachangle2,releaseangle3,approachangle3=f.angles(23,der1,der2,der3)
# twentythreeY1, twentythreeY2, twentythreeY3 = f.evalPoly(twentythreePoly1, twentythreePoly2, twentythreePoly3, x23)
# plt.subplot(1,3,2)
# f.plotPoly(twentythreeY1, twentythreeY2, twentythreeY3, x23)

# f.printFormatted(23, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3 = f.fitPolys(thirtysevenFeet)
# playerheight1, playerheight2, playerheight3= f.playerh(thirtysevenFeet)
# max1, max2, max3 = f.maxh(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3)
# der1, der2, der3 = f.derivatives(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3)
# releaseangle1,approachangle1,releaseangle2,approachangle2,releaseangle3,approachangle3=f.angles(37,der1,der2,der3)
# thirtysevenY1, thirtysevenY2, thirtysevenY3 = f.evalPoly(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3, x37)
# plt.subplot(1,3,3)
# f.plotPoly(thirtysevenY1, thirtysevenY2, thirtysevenY3, x37)

# f.printFormatted(37, releaseangle1, releaseangle2, releaseangle3, playerheight1, playerheight2, playerheight3, max1, max2, max3, approachangle1, approachangle2, approachangle3)

# thirtysevenY1, thirtysevenY2, thirtysevenY3 = f.evalPoly(thirtysevenPoly1, thirtysevenPoly2, thirtysevenPoly3, x37)

# plt.show()

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
