import math
import os
import time


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# Uses the function "cls" for clearing the console
cls()


firstNameString = 'Please insert your First Name: '
firstName = str(input(firstNameString).title())

lastNameString = 'Please insert your Last Name: '
lastName = str(input(lastNameString).title())

print('Welcome, {0} {1}. This is a python program!  :)'.format(firstName,lastName))

unitsMessage = '{0}, enter your units: '.format(firstName)
units = str(input(unitsMessage).lower())

radiusMessage = '{0}, enter your radius in {1}: '.format(firstName,units)
r = float(input(radiusMessage))

print('Thank you, {0}. Your radius is {1:.2f} {2}'.format(firstName,r,units))

print('Calculating the area and the circumference now...')

time.sleep(2)

area = math.pi * r ** 2
circumference = math.pi * 2 * r

print('For a radius of {0:.2f} {1}, the area is {2:.2f} {1}^2, while the circumference is {3:.2f} {1}.'.format(r, units, area, circumference))
print('Thank you, {0} {1}!'.format(firstName,lastName))