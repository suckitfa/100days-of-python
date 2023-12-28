def add_even(max):
    total = 0
    for number in range(1,max+1):
        if (number % 2 == 0):
            total += number
    return total

def add_even2():
    total = 0
    for num in range(2,101,2):
        total += num
    return total
result = add_even(100)
print(f"result = {result}")
result2 = add_even2()
print(f"result2 = {result2}")