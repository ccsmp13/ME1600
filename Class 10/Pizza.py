from terminalCLS import cls


cls()
print("************************************************")
print("          Welcome to SAMPSON'S PIZZA")
print("************************************************")
cost = []
reply = True
pizza = []


sumCost = 0
while(reply):
    selection = float(input("Choose a pizza: \n1. Cheese\n2. Pepperoni\n3. Ham\n4. Sausage\n5. Custom pizza (specify)\nSelect the pizza (1-5) or ask for total(6): "))
        
    match selection:
        case 1:
            pizza.append('Cheese')
            cost.append(10)
            sumCost += 10
            

        case 2:
            pizza.append('Pepperoni')
            cost.append(12)
            sumCost += 12

        case 3:
            pizza.append('Ham')
            cost.append(12)
            sumCost += 12
            
        case 4:
            pizza.append('Sausage')
            cost.append(12)
            sumCost += 12
            
        case 5:
            pizza.append(str(input("Please specify the custom pizza: ")).title())
            cost.append( 18)
            sumCost += 18
        
        case 6:
            reply = False
            
        case _:
            print("Error! Your pizza selection is invalid.")
        
        
if cost[0] != 0:
    print("************************************************")
    print("           THANK YOU FOR YOUR ORDER!")
    print("************************************************")
    for pizza,cost in zip(pizza,cost):
        print('{:37} : $ {:3.2f}'.format(pizza,cost))
    print("************************************************")
    print("{:37} : $ {:3.2f}".format("TOTAL", sumCost))
    print("************************************************")