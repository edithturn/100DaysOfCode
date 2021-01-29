def caesar(plain_text,shift_amount, dir):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if dir == "e":
            print("[ == Encrypting == ]")
            new_position = positon + shift_amount
        elif dir == "d":
            print("[ == Decrypting == ]")
            new_position = positon - shift_amount
        else:
            print("Please insert [e] and [d]")
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

direction = input("Type [e] to 'encode' to encrypt, type [d] to 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


encrypt(plain_text=text, shift_amount=shift,dir=direction )