prices =[100,200,300,400,500]

# normal way
doublePrices=[]
for price in prices :
    doublePrices.append(price*2)

print (doublePrices)

#comprehension way
ages = [1,2,3,4,5,6,7,8,9,10]
doubleAges = [age*2 for age in ages ]

print(doubleAges)


nums = [1,2,3,4,5,6,7,8,9,10]
evenDouble = [num*2 for num in nums if num%2==0]

print(evenDouble)


