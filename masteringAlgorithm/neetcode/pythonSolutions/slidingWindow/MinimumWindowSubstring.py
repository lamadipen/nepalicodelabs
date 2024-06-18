class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        countT={}
        need=0

        for item in t:
            countT[item] = 1+ countT.get(item,0)
            need +=1

        left=0
        have=0
        countS ={}
        minStr = float("inf")
        minStrArr = [-1,-1]

        for right in range(len(s)):
            target = s[right]

            if target in countT:
                countS[target] = 1+ countS.get(target,0)
                if countS[target] == countT[target]:
                    have+=1

            while have == need:
                if (right - left + 1) < minStr:
                    minStr = right -left +1
                    minStrArr = [left, right]

                if s[left] in countT:
                    countS[s[left]] = countS.get(s[left],0) - 1
                    if countS[s[left]] < countT[s[left]]:
                        have-=1
                left+=1
        l, r = minStrArr
        return s[l:r+1] if minStr != float("inf") else ""

solution = Solution()
actual1 = solution.minWindow("ADOBECODEBANC", "ABC")
print(actual1)
actual2 = solution.minWindow("a", "a")
print(actual2)
actual3 = solution.minWindow("a", "aa")
print(actual3)