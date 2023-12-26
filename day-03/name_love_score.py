# take both name to cal the num of times that "TRUE" ”LOVE“
print("Welcome to the love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is your name?\n")

def cal_love(name1,name2):
    name = name1 + name2
    low_case_name = name.lower()
    true_total = 0
    love_total = 0
    for l in "true":
        l_num = low_case_name.count(l)
        print(f'{l} accurs {l_num} times')
        true_total += l_num
    print(f"Total = {true_total}")

    for l in "love":
        l_num = low_case_name.count(l)
        print(f'{l} accurs {l_num} times')
        love_total += l_num
    print(f"Total = {love_total}")
    return int(f"{true_total}{love_total}")

love_socre = cal_love(name1,name2)
if (love_socre) < 10 or (love_socre) > 90:
    print(f"Your love score is {love_socre},you go togther like coke and mentors.")
elif love_socre >= 40 and love_socre <= 50:
    print(f"Your love score is {love_socre}, and you two are alright.")
else:
    print(f"Your score is {love_socre}")
