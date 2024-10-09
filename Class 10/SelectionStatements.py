import math






# weight = float(input("Enter the weight (lbs) of the package: "))
# print("Your package weighs {:.3} lbs.".format(weight))
# cost = 4

# if weight >= 5:
#     cost += math.ceil(weight - 5) * 1.25
# print("The total shipping cost is: {:.3} dollars".format(cost))


# carYear = int(input("Please enter the year your car was made: "))
    
# tax = 0
    
# if carYear <= 1996:
#     tax = 135
# elif carYear <= 2000:
#     tax = 100
# elif carYear <= 2004:
#     tax = 80
# elif carYear <= 2007:
#     tax = 54
# elif carYear <= 2014:
#     tax = 18
# else:
#     print("No tax is due")
    
    

# if tax != 0:
#     print("You owe {} dollars".format(tax))
    
    
    
    
print("***************************")
print("Welcome to SAMPSON'S PIZZA")
print("***************************")
selection = int(input("Choose a pizza: \n1. Cheese\n2. Pepperoni\n3. Ham\n4. Sausage\n5. Custom pizza (specify)\nSelect the pizza (1-5): "))
cost = 0
match selection:
    case 1:
        pizza = 'Cheese'
        cost = 10
    case 2:
        pizza = 'Pepperoni'
        cost = 12

    case 3:
        pizza = 'Ham'
        cost = 12
        
    case 4:
        pizza = 'Sausage'
        cost = 12
        
    case 5:
        pizza = str(input("Please specify the custom pizza: ")).title()
        cost = 12 + pizza.count(' ') * 2
    
    case _:
        print("Error! Please select an appropriate number (1-5)")
    
if cost != 0:
    print("***************************")
    print("THANK YOU FOR YOUR ORDER!")
    print("Preparing: {} pizza".format(pizza))
    print("Your total is {:.2f}".format(cost))
