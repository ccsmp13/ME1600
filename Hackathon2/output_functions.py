# Print the data the user entered to the terminal
def PrintData(sideA, slantS, units):
    print("**Squared pyramid problem: data**\n")
    print("Pyramid side = {:10.2f} {}".format(sideA,units))
    print("Slant Height = {:10.2f} {}".format(slantS, units))
    print("\n\n")

# Print the results to the terminal
def PrintResults(areaBase, surfaceArea, height, volume, units):
    print("**Squared pyramid problem: ressults**\n")
    print("Area Base = {:15.3f} {}^2".format(areaBase, units))
    print("Total Surface = {:11.3f} {}^3".format(surfaceArea, units))
    print("Height = {:18.3f} {}".format(height,units))
    print("Volume = {:18.3f} {}".format(volume, units))
    
