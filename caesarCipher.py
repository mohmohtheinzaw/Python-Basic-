alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Choice endcode or decode :")
message = input("Enter the message :")
shift = int(input("Enter the shift number : "))

def choice(direction) :
    if direction == "encode" :
        encode(message,shift)
    elif (direction == "decode") :
        decode (message,shift)
    else :
        print("please choose if you want to decode or encode correctly .")
        


def encode (text,shift_amount) :
    final_text = ""
    for char in text :
        if char in alphabet :
            position = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else :
            final_text += char
    print(f"Encode message is {final_text}")

def decode (text,shift_amount) :
    final_text = ""
    for char in text :
        if char in alphabet :
            position = alphabet.index(char)
            new_position = position - shift_amount
            final_text += alphabet[new_position]
        else :
            final_text += char
    print (f"Decode message is {final_text}")


# encode(message,shift)
# decode(message,shift)

choice(direction)




