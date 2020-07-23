def buy(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0.0


    for price in prices:
        sell_today = price - min_price
        max_profit = max(max_profit, sell_today)
        min_price = min(min_price, price)

    return max_profit


def bubub(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0.0

    for price in prices:
        sell_today = price - min_price
        max_profit = max(sell_today, max_profit)
        min_price = min(min_price, price)

    return max_profit

stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

print(buy(stock_prices))

print(bubub(stock_prices))
