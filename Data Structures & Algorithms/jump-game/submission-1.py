class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        rel = 0
        for i in range(1, len(range(len(nums)))):
            rel += 1
            if nums[i] >= rel:
                rel = 0
        return rel == 0