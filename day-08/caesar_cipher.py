alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    encrypt_text = ''
    len_alphabet = len(alphabet)
    for letter in text:
        # handle index outof range
        lt_index = (alphabet.index(letter) + shift) % (len_alphabet - 1)
        encrypt_text += alphabet[lt_index]
    print(f"The encoded text is {encrypt_text}")

# encrypt(text=text,shift=shift)

def decrypt(text,shift):
    decrypt_text = ''
    len_alphabet = len(alphabet)
    for letter in text:
        # handle index outof range
        lt_index = (alphabet.index(letter) - shift) % (len_alphabet - 1)
        decrypt_text += alphabet[lt_index]
    print(f"The decoded text is {decrypt_text}")

# decrypt(text=text,shift=shift)
    
if direction == 'encode':
    encrypt(text=text,shift=shift)
elif direction == 'decode':
    decrypt(text=text,shift=shift)
else:
    print("You type the woring deriction！")
