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