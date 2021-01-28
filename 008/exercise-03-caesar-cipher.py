def encrypt(text,shift):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    tmp_alphabeth = []

    for post in range(shift, len(alphabet)):
        tmp_alphabeth.append(alphabet[post])
    for pre in range(shift):
        tmp_alphabeth.append(alphabet[pre])
    
    index_text = 0
    
    while index_text in range(len(text)):
        index = 0
        while index in range(len(alphabet)):
            if text[index_text] == alphabet[index]:
                print(tmp_alphabeth[index])
                break
            index += 1
        index_text += 1


    print(alphabet)
    print(tmp_alphabeth)

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)