def trade_kadane(prices):
    if not prices:
        return 0

    lowest = float('inf')
    buy_price = None
    sell_price = None
    best_profit = 0

    for price in prices:
        profit = price - lowest

        if price < lowest:
            lowest = price


        if best_profit < profit:
            best_profit = profit
            sell_price = price
            buy_price = lowest


    return (best_profit, buy_price, sell_price)


stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

print(trade_kadane(stock_prices))