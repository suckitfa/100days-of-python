def get_BMI():
    weight = int(input("Your weight:"))
    height = float(input("Your height:"))
    bmi_num = int(weight / (height ** 2))
    return bmi_num

print(get_BMI())