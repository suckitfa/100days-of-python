print("wELCOME TO THE ROLLERCOASTER!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $4.")
    elif age <= 18:
        print("Plean pay $8")
    else:
        print("Please pay $18.")
else:
    print("Sorry, you have to grow taller before you can ride.")