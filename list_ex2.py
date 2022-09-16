books=['ramayana','mahabharat','half girlfriend','steelheart','calamity']

books.append('atomic habit')
books.append('you can win')
books.append('radhey')

books[6]='The well of Ascension'

books.insert(3,'legion:skin deep')

books.remove('half girlfriend')
print(' idx\t | books')
for i,b in enumerate(books):
    print(f'{i}\t {b}')

l1=['rahul','sonu']
l2=['aman','avinash']
l1.extend(l2)
print(l1)