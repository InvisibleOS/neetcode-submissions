class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        lo = 0
        hi = (rows * cols) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return False