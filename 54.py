class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        direction = "right"
        
        while(left < right and top < bottom):
            if direction == "right":
                for i in range(left, right):
                    ans.append(matrix[top][i])
                direction = "down"
                top += 1
            elif direction == "down":
                for i in range(top, bottom):
                    ans.append(matrix[i][right-1])
                direction = "left"
                right -= 1
            elif direction == "left":
                for i in range(right-1, left-1, -1):
                    ans.append(matrix[bottom-1][i])
                direction = "up"
                bottom -= 1
            elif direction == "up":
                for i in range(bottom-1, top-1, -1):
                    ans.append(matrix[i][left])
                direction = "right"
                left += 1
        
        return ans