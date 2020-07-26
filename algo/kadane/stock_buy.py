stock_prices = [310,315,275,295, 260, 270, 290, 230, 255, 250]

def buy_n_2(A):
    if not A:
        return 0

    m = 0
    for i in range(len(A)):
        for j in range(len(A[i + 1:])):
            if A[i + 1:][j] - A[i] > m:
                m = A[i+1:][j] - A[i]

    return m


def buy_n(prices):
    if not prices:
        return 0

    min_price, max_profit = float('inf'), 0.0

    for price in prices:
        sell_today = price - min_price

        max_profit = max(sell_today, max_profit)

        min_price = min(min_price, price)

    return max_profit


print(buy_n_2(stock_prices))
print(buy_n(stock_prices))

