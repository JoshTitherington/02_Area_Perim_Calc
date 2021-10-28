    
def num_check(question):


    print()
    print("**** Area Perimeter Calculator *****")
    print()

    # Start of calculator loop
    keep_going =""
    while keep_going == "":

        width = num_check("Width: ")
        height = num_check("Height: ")

        # Calculate area (width x height)
        area = width * height

        # Calculate perimeter (width + height) x 2
        perimeter = 2 * (width + height)

        # Output area and perimeter
        print("Perimeter: {:.2f} units".format(perimeter))
        print("Area: {:.2f} units".format(area))
        print()

        keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")

    
    