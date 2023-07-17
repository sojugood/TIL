from random import choice

color = open('color.txt', 'r', encoding='utf-8').read().split()
food = open('food.txt', 'r', encoding='utf-8').read().split()

print(choice(color) + ' ' + choice(food))