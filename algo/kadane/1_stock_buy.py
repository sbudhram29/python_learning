def buy(S):
    if not len(S):
        return 0

    max_profit = 0
    min_price = float('inf')
    sells = None, None



    for price in S:
        sell_now = price - min_price

        if sell_now > max_profit:
            max_profit = sell_now
            sells = min_price, price


        if min_price > price:
            min_price = price

    return max_profit, sells

stock_prices = [310,315,275,295, 260, 270, 290, 230, 255, 250]

print(buy(stock_prices))