def welcomeMessage(firstName, lastName):
    print('Welcome, {0} {1}. This is a python program!  :)'.format(firstName,lastName))

def echoValues(firstName,radMin,radMax,units):
    print('Thank you, {0}. Your radius range is {1:.2f}:{2:.2f} {3}'.format(firstName,radMin,radMax,units))

def finalMessage(firstName, lastName, units, radVector, areaVector, circumferenceVector):
    print('In {0} the radius are:'.format(units))
    print(radVector)

    print('In {0}^2 the areas are:'.format(units))
    print(areaVector)
    
    print('In {0} the circumferences are:'.format(units))
    print(circumferenceVector)
    print('Thank you, {0} {1}!'.format(firstName,lastName))
