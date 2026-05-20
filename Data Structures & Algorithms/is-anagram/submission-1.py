class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = []
        for i in s:
            letters.append(i)
        for i in t:
            if i in letters:
                letters.remove(i)
            else:
                return False
        if letters:
            return False
        else:
            return True