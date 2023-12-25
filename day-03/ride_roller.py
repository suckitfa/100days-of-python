print("wELCOME TO THE ROLLERCOASTER!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 4
        print("Please pay $4.")
    elif age <= 18:
        bill = 8
        print("Plean pay $8")
    else:
        bill = 18
        print("Please pay $18.")
else:
    print("Sorry, you have to grow taller before you can ride.")

wants_photo = input("Want photo taken?(Y or N): ")
if wants_photo == 'Y':
    bill += 3
print(f"Total pay: {bill}")