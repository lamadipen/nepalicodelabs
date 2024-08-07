class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxLen = 0

        for i in range(len(s)):
            # odd palindrome
            l,r=i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxLen < (r-l+1):
                    maxLen = (r-l+1)
                    result = s[l:r+1]
                l-=1
                r+=1
            # even palindrome
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if maxLen < (r-l+1):
                    maxLen = (r-l+1)
                    result = s[l:r+1]
                l-=1
                r+=1
        return  result


solution = Solution()
expected1 = ["aba","bab"]
actual1= solution.longestPalindrome("ababd")
print(actual1 in expected1)
expected2 = ["bb"]
actual2= solution.longestPalindrome("abbc")
print(actual2 in expected2)