# prompt user
apple = int(input("Please enter the quantity of apples you wish to purchase: "))

# check quantity
if apple < 10: 
    price = .75
elif apple >= 10 and apple < 50: 
    price = .5 
elif apple >= 50: 
    price = .5*.9

# print total cost
cost = apple*price
print(f'Your order of {apple} apples will cost ${cost}')