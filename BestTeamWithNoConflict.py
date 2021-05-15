'''
In this question we zip age and score to help ourselves to not compare ages again and again
'''

def bestTeam(sefl,age,scores):
    n = len(age)
    players = [[a,s] for a,s in zip(age,scores)]
    players = sorted(players, reverse=True)

    dp = [0]*n
    result = 0

    for i in range(n):
        score = players[i][1]
        dp[i] = score

        for j in range(i):
            if players[j][1]>=players[i][1]:
                dp[i] = max(dp[i],score+dp[j])

        ans = max(dp[i],ans)

    return ans