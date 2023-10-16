import random

trials = 1000000
fee = 1

money = 0

for _ in range(trials):

    money -= fee

    counter = 0

    while True:
        coin = random.randint(0, 1)
        if coin == 0:
            break
        counter += 1

    winnings = 2**counter
    money += winnings

print(money)