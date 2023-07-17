import os
f = open('postcard.txt')
lines = f.readlines()
for i in lines[3:9]:
    words = i.split()
    first_two_words = ' '.join(words[:2])
    print(first_two_words.replace('.', '').replace(',', '').replace(':', '').upper(), end=' ')