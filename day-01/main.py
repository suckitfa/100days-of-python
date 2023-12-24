print("Hello world!")
print('Hello world !\nHello world!')
print("Hello" + " "+"Angela")
#  print("hell world") // IndentationError: unexpect indent
your_name = input("What's your name:")
print("Your name is: " + your_name)

def get_your_band_name():
    your_city = input("what's your city:")
    your_dog_name = input("What's your dog's name:")
    print("You band name could be: ",f'{your_city} {your_dog_name}.')

get_your_band_name()