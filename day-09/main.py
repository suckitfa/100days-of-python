import art

print(art.logo)
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary['Bug'])

# add new items
programming_dictionary['Loop'] = 'Loop is reaptly doing something.'
print(programming_dictionary['Loop'])

#  create an empty dict
# empty_dict = {}
# wipe an exsiting dict
# programming_dictionary = {}

for thing in programming_dictionary:
    print(thing)