
def num_check(question):
    valid = False

    print(question)
    
    while not valid:
        response = float(input("Enter a number: "))

        if response > 0:
            valid = True
        else: 
            print("Please enter a number greater than 0.")
        
    return response

#Main program
print()
print("**** Area Perimeter Calculator *****")
print()

width = num_check("Width: ")
height = num_check("Height: ")
price = num_check("Price: ")

perimeter = 2 * (width + height)

cost = perimeter * price

print("Perimeter: {:.2f} units".format(perimeter))
print("Cost: {:.2f} units".format(cost))
print()
print()
print("Thanks for using the fence calculator")









keep_going = input("press <enter> to keep going ot any key to quit")

print()
print("-" * 30)
print()