class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s=collections.Counter(nums)
        n=len(set(nums))
        line=list(s.items())
        line.sort(key=lambda x: x[1], reverse=True)
        result=[]
        for i in range(k):
            result.append(line[i][0])
            
        return result