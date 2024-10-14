from numpy.polynomial import polynomial as ply
import numpy as np
import matplotlib.pyplot as plt

coefficients=[-2,-3/2,3/4,1/4]
fx = ply.Polynomial(coefficients)
x = np.linspace(-6,6,1000)
y = fx(x)
xValue = 3
yValue = fx(xValue)
figure_1=plt.figure(1)
f_0 = ply.Polynomial.roots(fx) # roots calculates the roots of the polynomial
f_r = fx(f_0)
plt.plot(x,y)
plt.plot(xValue,yValue,"k+")
plt.plot(f_0,f_r,"or")

title = "f(x)= {}\n".format(fx)
title += " x={} is: {}\n".format(xValue,yValue)
title += "roots:[{}]".format(f_0)

plt.title(title)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()