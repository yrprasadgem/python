#print string as stack 
class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)
        print(stack)
        return True               
sln = Solution()
result = sln.isValid("Prasad*****SriVatsava")
print(result)