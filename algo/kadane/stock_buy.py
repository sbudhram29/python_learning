stock_prices = [310,315,275,295, 260, 270, 290, 230, 255, 250]


def buy_n(prices):
    if not len(prices):
        return 0

    min_price, max_profit = float('inf'), 0

    for price in prices:
        max_profit = max(max_profit, price-min_price)
        min_price = min(min_price, price)

    return max_profit, min_price

print(buy_n(stock_prices))

