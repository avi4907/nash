def total(a, b=3, c=0):
    return a+ b+ c

print(total(5))
print(total(a=5))

print(total(100,50))
print(total(b=50, a=100))

print(total(10, c=10, c=10))