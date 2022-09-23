# WAP to find the most occuring alphabet and its frequency
from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

freq=0
freq_letter =''
for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')
    if freq < counter:
        freq=counter
        freq_letter=letter
print(f'most frequent letter is {freq_letter} occurs {freq} times')