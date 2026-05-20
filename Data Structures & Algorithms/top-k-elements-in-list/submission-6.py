class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
            
        arr = []
        
        for j in range(k):
            # Because we delete keys as we go, the first key is always a new, valid candidate
            largest = list(map.keys())[0]
            
            for i in map.keys():
                if map[i] > map[largest]:
                    largest = i
            
            arr.append(largest)
            del map[largest] # Remove the winner so it is never checked again


        return arr



