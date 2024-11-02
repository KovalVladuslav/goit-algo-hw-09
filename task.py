def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

# Приклад використання
amount = 113
print("Жадібний алгоритм:", find_coins_greedy(amount))

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Ініціалізуємо список для зберігання мінімальної кількості монет для кожної суми від 0 до amount
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Для суми 0 не потрібно жодної монети

    # Масив для зберігання використаних монет для побудови рішення
    used_coins = [0] * (amount + 1)

    # Проходимо по кожній сумі до amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    # Побудуємо словник з використаними монетами
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = used_coins[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Приклад використання
amount = 113
print("Динамічне програмування:", find_min_coins(amount))

