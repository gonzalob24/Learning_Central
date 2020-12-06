import math


def coinChange(coins, change):
    # set up a counter to keep track of coins used
    number_of_coins_used = 0

    # reverse coins array coins = coins[::-1]
    coins = coins[::-1]

    for coin in coins:
        if change // coin > 0:
            number_of_coins_used += (change // coin)
            change = change % coin
        if change == coin:
            number_of_coins_used += 1
            break
    return number_of_coins_used


print(coinChange([1, 2, 5, 10, 20, 50, 100, 500, 1000], 2045))
