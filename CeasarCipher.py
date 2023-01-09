alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g',
'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(direction,text,shift_amount) :
    final_text = ""
    if direction  == "decode" :
        shift_amount = shift_amount * -1
    for char in text : 
        if char in alphabet :
            position  = alphabet.index(char)
            new_position = position + shift_amount
            final_text += alphabet[new_position]
        else :
                final_text += char
    print(f"{direction}ed message is {final_text}")  

is_end = False
while not is_end :
        direction = input("Choice endcode or decode :")
        message = input("Enter the message :")
        shift = int(input("Enter the shift number : "))
        shift = shift %26
        caesar(direction,message,shift)

        restart = input("Do you wanna continue: yes or no :")
        if restart == 'no' : 
            is_end = True
            print("Thanks !")


        