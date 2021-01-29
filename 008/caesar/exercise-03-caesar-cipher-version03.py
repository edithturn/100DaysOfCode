import art
print(art.logo)

def caesar(plain_text,shift_amount, dir):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    cipher_text = ""
    for letter in plain_text:        
        if letter in alphabet:
            position = alphabet.index(letter)
            if dir == "e":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(cipher_text)



option = True
while option == True:
    direction = input("Type [e] to 'encode' to encrypt, type [d] to 'decode' to decrypt:\n")
    while direction != "e" and direction != "d":
        print("Please insert [e] or [d]")
        direction = input("Type [e] to 'encode' to encrypt, type [d] to 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        print("Out of range, choose a number less than 26")
        shift = int(input("Type the shift number:\n"))
    caesar(plain_text=text, shift_amount=shift,dir=direction )

    result = input("Do you want to continue? [Y] Yes or [N] Not\n")
    if result.lower() == "n":
        option = False
        print("GoodBye")
        
    
