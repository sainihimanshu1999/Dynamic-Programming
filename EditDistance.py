'''
This question is done by both memoization and tabulation form, i'll write all three solutions below
'''

'''
Naive Soltuion
'''

def edit(self,word1,word2):
    if not word1 and not word2:
        return 0

    if not word1:
        return len(word2)

    if not word2:
        return len(word1)

    if word1[0] == word2[0]:
        return self.edit(word1[1:],word2[1:])
    else:
        insert = 1+ self.edit(word1,word2[1:])
        delete = 1+self.edit(word1[1:],word2)
        replace = 1+ self.edit(word1[1:],word2[1:])

        return min(insert,replace,delete)


'''
Memoization
'''

def edit2(self,word1,word2):
    def dist(word1,word2,i,j,memo):
        if i == len(word1) and j==len(word2):
            return 0

        if i == len(word1):
            return len(word2)-j

        if j == len(word2):
            return len(word1)-i

        if (i,j) not in memo:
            if word1[i] == word2[j]:
                ans = dist(word1,word2,i+1,j+1,memo)

            else:
                insert = 1 + dist(word1,word2,i,j+1,memo)
                delete = 1 + dist(word1,word2,i+1,j,memo)
                replace = 1+ dist(word1,word2,i+1,j+1,memo)
                ans = min(insert,delete,replace)
            memo[(i,j)] = ans
        return memo[(i,j)]

    return self.edit2(word1,word2,0,0,{})


'''
Tabulation 
'''

def edit3(self,word1,word2):
    m = len(word1)
    n = len(word2)

    grid = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        grid[i][0] = i
    
    for j in range(n+1):
        grid[0][j] = j


    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                grid[i][j] = grid[i-1][j-1]

            else:
                grid[i][j] = 1+ min(grid[i-1][j],grid[i][j-1],grid[i-1][j-1])

    return grid[-1][-1]