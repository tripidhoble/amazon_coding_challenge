
class Solution:
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        left, top = 0, 0
        right, down = c-1, r-1    
        cnt = 1
        arr = []
        direction = 0
        while cnt <= r*c:
            if direction == 0:
                for i in range(left,right+1):
                    arr.append(matrix[top][i])
                    cnt+=1
                top += 1
            elif direction == 1:
                for i in range(top,down+1):
                    arr.append(matrix[i][right])
                    cnt+=1
                right-=1
            elif direction == 2:
                for i in range(right,left-1, -1):
                    arr.append(matrix[down][i])
                    cnt+=1
                down-=1
            elif direction == 3:
                for i in range(down,top-1, -1):
                    arr.append(matrix[i][left])
                    cnt+=1
                left+=1
            
            if direction == 3:
                direction = 0
            else:
                direction += 1 
                
        return arr

matrix =  [[1,  2,  3,  4],
           [5,  6,  7,  8],
           [9,  10, 11, 12],
           [13, 14, 15, 16]]

obj = Solution()
obj.spirallyTraverse(matrix,4,4)
