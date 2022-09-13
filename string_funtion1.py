msg = "we will be seeing the horizon"
 
words = msg.split()
print(words)

words = msg.split('e')
print(words)

#Replace

update_msg = msg.replace('seeing','viewing')
print(update_msg)

#Join

path = ['aman','avinash','mypc']
content = '/'.join(path)
print(content)

#Strip()

name ='     Avinash     '
cleaned_name = name.strip()
print(cleaned_name)

# WAP to find frequency of all the vowels in the files
from helper import read
data = read('pride_n_prejudice.txt')

for vowel in 'aeiou':
    print(f'{vowel} => {data.lower().count(vowel)} times')

# WAP to remove all the punctations from the string
str='he@#ll%o!@&*(!@wo!@r,l!d)'

from string import punctuation
for p in punctuation:
    str=str.replace(p,'')
print(str)