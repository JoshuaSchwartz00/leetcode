class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        answer = []
        for i in range(n):
            answer.append([0]*n)
        upper, lower, left, right = 0, n, 0, n
        num = 1
        
        while(num <= n*n):
            for i in range(left, right):
                answer[upper][i] = num
                num += 1
            upper += 1
            
            for i in range(upper, lower):
                answer[i][right-1] = num
                num += 1
            right -= 1
            
            for i in range(right-1, left-1, -1):
                answer[lower-1][i] = num
                num += 1
            lower -= 1
            
            for i in range(lower-1, upper-1, -1):
                answer[i][left] = num
                num += 1
            left += 1
        
        return answer