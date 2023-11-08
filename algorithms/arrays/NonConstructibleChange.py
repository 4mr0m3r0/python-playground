# Big O Notation. Time O(n log n) | Space O(1).
def non_constructible_change(coins):
    coins.sort()
    amountChange = 0
    for coin in coins:
        if amountChange + 1 < coin:
            return amountChange + 1
        amountChange += coin
    return amountChange + 1
