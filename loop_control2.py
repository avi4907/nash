while True:
    price = int(input('enter price of item:'))
    if price < 0:
        break
    print (f'you entered {price} amount')

x=[1,2,3,4,5,6,7,-3,34,56]
for i in x:
    if i < 0:
        break
    print(i)