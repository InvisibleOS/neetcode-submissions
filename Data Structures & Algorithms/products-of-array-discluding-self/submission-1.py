class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        prod = 1
        for i, val1 in enumerate(nums):
            for j, val2 in enumerate(nums):
                if i != j:
                    prod *= val2
            arr.append(prod)
            prod = 1

        return arr