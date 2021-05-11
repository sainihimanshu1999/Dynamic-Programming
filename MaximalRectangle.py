def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        col = len(matrix[0])
        heights = [0]*(col+1)
        area = 0
        
        for row in matrix:
            for j in range(col):
                heights[j] = heights[j]+1 if row[j]== '1' else 0
                
                
            stack = [-1]
            for i,height in enumerate(heights):
                while heights[stack[-1]]>height:
                    h = heights[stack.pop()]
                    w = i-stack[-1]-1
                    area = max(area, h*w)

                stack.append(i)

            
        return area