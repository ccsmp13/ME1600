# Find the final temperature of gear and water
# during a quenching process
#
#Collin Sampson
#9/9/24
massMetal = 5.0
tempInitialMetal = 150.0
volumeWater = .002
tempInitialWater = 10.0 
specHeatMetal = .5
specHeatWater = 4.2
density = 1000

# massMetal = 5.0
# tempInitialMetal = 150.0
# volumeWater = .002
# tempInitialWater = 10.0 
# specHeatMetal = .5
# specHeatWater = 4.2
# density = 1000

# massMetal = 5.0
# tempInitialMetal = 150.0
# volumeWater = .002
# tempInitialWater = 10.0 
# specHeatMetal = .5
# specHeatWater = 4.2
# density = 1000


massWater = density * volumeWater

tempFinalMetal = massMetal * specHeatMetal
sideOne = massMetal * specHeatMetal * tempInitialMetal
sideTwo = massWater * specHeatWater * tempInitialWater
tempFinalWater = massWater * specHeatWater


tempFinal = tempFinalMetal + tempFinalWater
sideTwo = sideTwo + sideOne
result = sideTwo / tempFinal

print('The mass of the metal is {0:5.4f}'.format(massMetal))
print('The intiial temperature of the metal is {0:.4f}'.format(tempInitialMetal))
print('The volume of the water is {0:5.4f}'.format(volumeWater))
print('The intiial temperature of the water is {0:5.4f}'.format(tempInitialWater))
print('The final temperature will be {0:5.4f}'.format(result))