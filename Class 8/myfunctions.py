import numpy as np
import matplotlib.pyplot as plt

def askrange():
    minVal = int(input("Please enter a minimum value of x: "))
    maxVal = int(input("Please enter a maximum value of x: "))
    x = np.linspace(minVal,maxVal, 100)
    return x
    
def calc_sc(x):
    f = np.sin(x)
    k = np.cos(x)
    return f,k

def plotall(f,k,x):
    figure_1 = plt.figure(1)
    plt.subplot(1,2,1)
    plt.plot(x,f,'r:')
    plt.title("sine function")
    plt.ylabel("sin(x)")
    plt.xlabel("x")
    
    plt.subplot(1,2,2)
    plt.plot(x,k,'b+')
    plt.title("cosine function")
    plt.ylabel("cos(x)")
    plt.xlabel("x")
    
    figure_2 = plt.figure(2)
    plt.plot(x,f,'r:')
    plt.plot(x,k,'b+')
    plt.ylabel("sin(x) and cos(x)")
    plt.legend(["sin(x)", "cos(x)"])
    plt.title("sine and cosine function")
    plt.xlabel("x")
    
    figure_1.savefig("graph1.png", dpi = 600)
    figure_2.savefig("graph2.png", dpi = 600)
    plt.show()