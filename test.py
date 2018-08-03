import random

answer=random.randint(-1,36)
print answer
if answer in (-1, 0):
    color = 'Green'
elif answer in (1, 3, 5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35):
    color = "Red"
elif answer in (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,36):
    color = "Black"

print (color)
