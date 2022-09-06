for i in range(100):
    print('hey avi',i)

for i in range(10,21):
    print(i,end=' ')

for i in range(1,11,2):
    print(i, end=' ')

#Reverse loop

for i in range(100,0,-1):
    print(i, end=' ')

print('=>')
data=[2,3,4,5,6,6,7,87,8,9,5]
for i,d in enumerate(data):
    print(i,d)

names=['laptop','mobile','keyboard']
prices=[59999,9999,399]    
for n,p in zip(names,prices):
    print(f'{n} => ${p}')