#Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', '}':'{', ']' :'['}

        for item in s:
            if item in map:
                if stack and stack[-1] == map[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        print(stack)
        return True if not stack else False

solution = Solution()
result1 = solution.isValid('()[]{}')
print(result1)
result2 = solution.isValid('([])')
print(result2)
result3 = solution.isValid('(]')
print(result3)
result4 = solution.isValid('((')
print(result4)