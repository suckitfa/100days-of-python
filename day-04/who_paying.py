import random
name_str = input("Give everybody's name, seperated by comma.")
names = name_str.split(',')
# print(names)
choosed_person = random.choice(names)
print(f"{choosed_person} is going to pay the bill.") 