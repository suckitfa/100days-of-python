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

def caesar(start_text, shift_amount, cipher_direction): 
    if cipher_direction == 'decode':
        shift = shift_amount * -1
    elif cipher_direction == 'encode':
        shift = shift_amount
    else:
        print("woring direction!")
        return
    encrypt_text = ''
    len_alphabet = len(alphabet)
    for letter in start_text:
        # handle index outof range
        lt_index = (alphabet.index(letter) + shift) % (len_alphabet - 1)
        encrypt_text += alphabet[lt_index]
    print(f"The {cipher_direction} text is {encrypt_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)