class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        print(sort)
        sort2 = []
        for i, val in enumerate(sort):
            if val not in sort2:
                sort2.append(val)
        x = 0
        streak = 0
        max = 0
        for i in sort2:
            if i-1 not in sort2:
                streak = 0
                j=0
                while i+j in sort2:
                    streak += 1
                    j += 1
                if streak > max:
                    max = streak
        return max