class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            elif i in pairs.values():
                if stack and pairs[stack[-1]] == i:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else:
            return True
        
obj = Solution()
print(obj.isValid("]"))