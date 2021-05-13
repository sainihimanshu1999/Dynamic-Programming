'''
In this question we have 3 states, hold, not hold, cooldown, initially the hold and cooldown value will
be meaningless i.e float('-inf'), only not hold will be meaningful
'''

def stock(self,price):
    hold,notHold,cooldown = float('-inf'),0,float('-inf')

    for p in prices:
        hold,notHold,cooldown = max(hold,notHold-p), max(notHold,cooldown), hold+p

    return max(notHold, cooldown)