class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ""
        for i in s.casefold():
            if i.isalnum():
                k += i

        i = 0
        j = len(k) - 1

        while i <= j:
            if k[i] != k[j]:
                return False
            else:
                i += 1
                j -= 1
        return True