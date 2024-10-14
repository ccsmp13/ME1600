from numpy.polynomial import Polynomial as ply
import numpy as np
import matplotlib.pyplot as plt


Fx = ply([11.1136, -4.4942, .8575, -.0495, .0009])
der_Fx = Fx.deriv()
critPoints = ply.roots(der_Fx)
critPointsEval = Fx(critPoints)

der_der_Fx = der_Fx.deriv()
pointsOfInflection = ply.roots(der_der_Fx)
pointsOfInflectionEval = Fx(pointsOfInflection)

x = np.linspace(0,25,1000)
y = Fx(x)

plt.plot(x,y,"b")
plt.plot(critPoints,critPointsEval,"ro")
plt.plot(pointsOfInflection,pointsOfInflectionEval,"k*")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(f"f(x)= {Fx}")

plt.show()
