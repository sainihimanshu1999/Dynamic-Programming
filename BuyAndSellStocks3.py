'''
In this question maximum 2 transaction is allowed and buying should be done after first selling, that's 
why we maintained the profits array 
'''

def stock(self,prices):
    minPrice = float('inf')
    maxProfit = 0
    profits = []

    for price in prices:
        minPrice = min(minPrice,price)
        profit = price-minPrice
        maxProfit = max(profit,maxProfit)
        profits.append(maxProfit)

    maxProfit = 0
    total = 0
    maxPrice = float('-inf')

    for i in range(len(prices))[::-1]:
        maxPrice = max(maxPrice,prices[i])
        profit = maxPrice - prices[i]
        maxProfit = max(maxProfit,profit)
        total = max(total,maxProfit+profits[i])
    return total