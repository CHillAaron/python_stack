# 72

def coin_change(num):
    quart = 0
    dime = 0
    nick = 0
    penny = 0
    while num > 0:
        if num >= 25:
            num -= 25
            quart += 1
        elif num >= 10:
            num -= 10
            dime += 1
        elif num >= 5:
            num -= 5
            nick += 1
        else:
            num -= 1
            penny += 1
    print(f"quarter = {quart}, dime = {dime}, nickles = {nick}, pennies = {penny}")

coin_change(70)