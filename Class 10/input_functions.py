def name():
    firstNameString = 'Please insert your First Name: '
    firstName = str(input(firstNameString).title())

    lastNameString = 'Please insert your Last Name: '
    lastName = str(input(lastNameString).title())
    return(firstName,lastName)

def units(firstName):
    unitsMessage = '{0}, enter your units: '.format(firstName)
    units = str(input(unitsMessage).lower())
    return units

def radius(firstName, units):
    radiusMessage = '{0}, enter your radius in {1}: '.format(firstName,units)
    r = float(input(radiusMessage))
    return r

def rangeStepRadius(firstName, units):
    minRadiusMessage = '{0}, enter then first radius in {1}: '.format(firstName,units)
    minRad = float(input(minRadiusMessage))
    maxRadiusMessage = '{0}, enter then last radius in {1}: '.format(firstName,units)
    maxRad = float(input(maxRadiusMessage))
    stepSizeMessage = '{0}, enter the step in {1}: '.format(firstName, units)
    stepSize = float(input(stepSizeMessage))
    return minRad, maxRad, stepSize