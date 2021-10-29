
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

area = width * height

perimeter = 2 * (width + height)

print("Perimeter: {:.2f} units".format(perimeter))
print("Area: {:.2f} units".format(area))
print()
print()
print("Thanks for using the area / perimeter calculator")

    
    