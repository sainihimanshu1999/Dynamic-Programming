'''
We use simple iterative solution, A part of code is written in single line only to keep 1st value intact
'''

def HouseRobber(self,houses):
    dp1 = 1
    dp2 = 0
    for house in houses:
        dp1,dp2 = dp2,max(dp1+num,dp2)

    return dp2
