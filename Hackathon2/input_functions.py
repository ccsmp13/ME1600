
# Ask the user for the units they are using
def ask_units():
    units = str(input("Which are the units for this problem? ").lower())
    return units

# Ask the user for the side length and the slant length
def ask_lengths(units):
    sideLength = float(input("What is the side, a, of this squared pyramid in {0}? ".format(units)))
    slant = float(input("What is the slant height, S, of this squared pyramid in {0}? ".format(units)))
    print("\n\n\n\n")
    return slant, sideLength