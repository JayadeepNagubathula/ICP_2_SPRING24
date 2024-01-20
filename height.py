inches =[] #creating empty list
print ("Enter heights in inches. Type 'done' when finished.") 
while True:
    x = input("Enter height in inches(or 'done' to finish): ") # taking input from the user
    if x.lower() == 'done':
        break
    try:
        height_inch = float(x) 
        inches.append(height_inch) # adding the given inches to empty list
    except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
centimeters = [height * 2.54 for height in inches] #converting the inches to centimetres
print("Heights in Inches:", inches) #printing the inches in list
print("Heights in centimeters:", centimeters) #printing the centimetres in list
