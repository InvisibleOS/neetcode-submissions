class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        water = 0
        current = 0
        
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                floor_index = stack.pop()
                if not stack:
                    break
                left_index = stack[-1]
                right_index = current
                width = right_index - left_index - 1
                bounded_height = min(height[left_index], height[right_index]) - height[floor_index]
                water += width * bounded_height
            stack.append(current)
            current += 1
        return water