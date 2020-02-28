class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "[" }
        for char in s:
            if char in mapping:
                if len(stack) > 0:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if(mapping[char] != top_element):
                    return False
            else:
                if char in ["(", "{", "["]:
                    stack.append(char)
        if(len(stack) > 0):
            return False
        else:
            return True
sln = Solution()
result = sln.isValid("(")
print(result)