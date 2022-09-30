nums=[1,2,34,5,67,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,9,8,7,65,4,3,2,1]
names=['Avinash Singh','Bulla Khulla','Abdur Rahman']


num_sqr=list(map(lambda i:i **2, nums))
print(num_sqr)

num_eq1 = list(map(lambda i : i+4 * i**2, nums))
print(num_eq1)

first_names = tuple(map(lambda nm : nm.split()[0], names))
print(first_names)