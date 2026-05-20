class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        string = ""
        for i,val in enumerate(s):
            if val in string:
                string = string[string.find(val)+1:]
            string += val
            if len(string) >= count:
                count = len(string)
        return count