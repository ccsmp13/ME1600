def welcomeMessage(firstName, lastName):
    print('Welcome, {0} {1}. This is a python program!  :)'.format(firstName,lastName))

def echoValues(firstName,radMin,radMax,stepSize,units):
    print('Thank you, {0}. Your radius range is {1:.2f}:{2:.2f}:{3:.2f} {4}'.format(firstName,radMin,radMax, stepSize,units))

def finalMessage(firstName, lastName, units, radVector, areaVector, circumferenceVector):
    
    message = 'Radius =     {:.2f} {}     Area =     {:.3f} {}^2     Circumference =     {:.3f} {}'
    for r,a,c in zip(radVector, areaVector, circumferenceVector):
        print(message.format(r,units, a, units, c, units))
    print('Thank you, {} {}!'.format(firstName,lastName))

