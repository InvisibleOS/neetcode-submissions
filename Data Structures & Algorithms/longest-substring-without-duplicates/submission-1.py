class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        string = ""
        for i,val in enumerate(s):
            if val in string:
                index = string.find(val)
                string = string[index+1:]
            string += val
            if len(string) >= count:
                count = len(string)
        return count