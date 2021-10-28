# functions go here

# checks input is a number more than zero
def num_check(question):    




# Main Routine goes here
width = num_check("Width: ")
height = num_check("Height")

# Calculate area (width x height)
area = width * height

# Calculate perimeter (width + height) x 2
perimeter = 2 * (width + height)

# Output area and perimeter
print("Perimeter: {} units".format(perimeter))
print("Area: {} units".format(area))