print("Welcome to the tip calculator.")
total = input("What was the total bill?")
num_of_people = input("How many people to splite the bill?")
tip_percent = input("What percentage tip would like to give? 10,12 or 15?")
avg = (float(total) * (1 + 0.01 * float(tip_percent))) / float(num_of_people)
print("Each person should pay:$"+str(avg))