import matplotlib.pyplot as plt

# print minVal, maxVal, thickness, tankDensity, and liquidDensity in the terminal
def print_data(minVal, maxVal, thickness, tankDensity, liquidDensity):
    print("Data for the tank optimization problem:")
    print("Minimum internal volume: {0:.2} m^3".format(minVal))
    print("Maximum internal volume: {0:.2f} m^3".format(maxVal))
    print("Thickness of the tank: {0:.2f} m".format(thickness))
    print("Tank material density: {0:.2f} kg/m^3".format(tankDensity))
    print("Tank liquid density: {0:.2f} kg/m^3".format(liquidDensity))
    print("+++++++++++++++++++++++++++++++++++++")

# Create 2 subplots that plot the length and the weight. 
def plot_length_weight(v_internal, D, A, weight_A, weight_D ):
    figure_1 = plt.figure(1)
    plt.subplot(1,2,1)
    plt.plot(v_internal,D,'b')
    plt.plot(v_internal,A,'r')
    plt.title("Tanks Maximum Dimension")
    plt.ylabel("D and A [m]")
    plt.xlabel("V_internal [m^3]")
    plt.legend(["Spherical tank diameter", "Cubical tank side"])
    
    plt.subplot(1,2,2)
    plt.plot(v_internal,weight_D,'b')
    plt.plot(v_internal,weight_A,'r')
    plt.title("Tanks Total Weight")
    plt.ylabel("Tanks Total Weight [N]")
    plt.xlabel("V_internal [m^3]")
    plt.tight_layout()
    plt.legend(["Spherical tank", "Cubical tank"])
    plt.show()