'''
In this question we buy and sell stocks only one time and maximize our profit, asses the min price and 
retain the max profit
'''

def stocks(self,prices):
    maxProfit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price,price)
        profit = price - min_price
        maxProfit = max(maxProfit,price)

    return maxProfit