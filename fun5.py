def mean(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)

mean(1,2,3,4)
print(mean(1,22,33,5,6,7,8,9))
print(mean())
