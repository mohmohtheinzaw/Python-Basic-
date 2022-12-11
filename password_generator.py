import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','(','&',')','*','-','+']

letter_amount = int(input("Enter the amount of letter :"))
nums_amount = int(input("Enter the amount of number :"))
symbols_amount = int(input("Enter the amount fo symbols :"))

letters_list = []
numbers_list = []
symbols_list = []

for i in range(0,letter_amount) :
    letter = letters[random.randint(0,len(letters)-1)]
    letters_list.append(letter)

for i in range(0,nums_amount) :
    number = numbers[random.randint(0,len(numbers)-1)]
    numbers_list.append(number)

for i in range(0,symbols_amount) :
    symbol = symbols[random.randint(0,len(symbols)-1)]
    symbols_list.append(symbol)


password = letters_list + numbers_list + symbols_list
random.shuffle(password)
password_str = "".join(password)

print(f'Your Password is : {password_str}')