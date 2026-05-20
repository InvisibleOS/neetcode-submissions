class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = []
        for i in nums:
            if i not in record:
                record.append(i)
                print(record)
            else:
                return True
        return False