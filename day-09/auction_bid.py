import art

name_bid = {}

def get_bid():
    print(art.logo)
    name = input("Enter you name:")
    bid = int(input("Your bid:"))
    name_bid[name] = bid
    has_next = input("next bid? yes or no")
    return has_next

def get_highest_bid():
    max_bid = 0
    for name in name_bid:
        cur_bid = name_bid[name]
        if cur_bid > max_bid:
            max_bid = cur_bid
    return max_bid
while get_bid() == 'yes':
    pass

print('name_bid = ',name_bid)
highest_bid = get_highest_bid()
print(f"THe highest bid is {highest_bid}")
print('bid over')