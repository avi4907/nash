x=[1,2,3,4,0,6,7,0,9,0,12]
for i in x:
    if i == 0:
        continue
    print(i)

#Continue with while

i = 1
while i <=5:
    data = input ('enter data:')
    if len (data) == 0:
        continue
    print(f'you entered a value of size{len(data)}')
    i += 1