def welcomeMessage(firstName, lastName):
    print('Welcome, {0} {1}. This is a python program!  :)'.format(firstName,lastName))

def echoValues(firstName,r,units):
    print('Thank you, {0}. Your radius is {1:.2f} {2}'.format(firstName,r,units))

def finalMessage(firstName, lastName, units, r, area, circumference):
    print('For a radius of {0:.2f} {1}, the area is {2:.2f} {1}^2, while the circumference is {3:.2f} {1}.'.format(r, units, area, circumference))
    print('Thank you, {0} {1}!'.format(firstName,lastName))
    
