import random

bet_amount = 10

#Red list
reds = "Red,"*18
reds = reds[:-1]
red_list = reds.split(',')

#Black list
black = "Black,"*18
black = black[:-1]
black_list = black.split(',')

#Zeros
zeros =["0"]
values = zeros+red_list+black_list
double_zeros =["00"]
values_two = zeros+double_zeros+red_list+black_list

#Initialize variables
win_amount = 0
count = 0
red_amt = 0
black_amt = 0
rand_amt = 0
red_amt_doub = 0
black_amt_doub = 0

print('|--------------------------------------------------------------------------|')
print("|   Simulation -1 (Single 0 - Always pick Red: Play 5 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')

while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -1 (Single 0 - Always pick Black: Play 5 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -1 (Single 0 - Always pick Red or Black: Play 5 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))


print('|--------------------------------------------------------------------------|')
print("|   Simulation -1 (Double 0 - Always pick Red: Play 5 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')

win_amount=0
count=0
while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -1 (Double 0 - Always pick Black: Play 5 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -1 (Double 0 - Always pick Red or Black: Play 5 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 5:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

#simulation -2
print('|--------------------------------------------------------------------------|')
print("|   Simulation -2 (Single 0 - Always pick Red: Play 100 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')
win_amount=0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -2 (Single 0 - Always pick Black: Play 100 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -2 (Single 0 - Always pick Red or Black: Play 100 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))


print('|--------------------------------------------------------------------------|')
print("|   Simulation -2 (Double 0 - Always pick Red: Play 100 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')

win_amount=0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -2 (Double 0 - Always pick Black: Play 100 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -2 (Double 0 - Always pick Red or Black: Play 100 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 100:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

#simulation -3
print('|--------------------------------------------------------------------------|')
print("|   Simulation -3 (Single 0 - Always pick Red: Play 1000 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')

while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -3 (Single 0 - Always pick Black: Play 1000 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -3 (Single 0 - Always pick Red or Black: Play 1000 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))


print('|--------------------------------------------------------------------------|')
print("|   Simulation -3 (Double 0 - Always pick Red: Play 1000 rounds of Roulette   | ")
print('|--------------------------------------------------------------------------|')

win_amount=0
count=0
while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Red":
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|--------------------------------------------------------------------------|')
print("|   Simulation -3 (Double 0 - Always pick Black: Play 1000 rounds of Roulette | ")
print('|--------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == "Black" :
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))

print('|---------------------------------------------------------------------------------|')
print("|   Simulation -3 (Double 0 - Always pick Red or Black: Play 1000 rounds of Roulette | ")
print('|---------------------------------------------------------------------------------|')

win_amount = 0
count=0
while count < 1000:
    answer = random.randint(0, 36)
    count += 1
    if values_two[answer] == random.choice(["Black", "Red"]):
        win_amount = win_amount + bet_amount
    else:
        win_amount = win_amount - bet_amount
print(" You won: " + str(win_amount))