class Solution:
    def validAnagram(self, s:str, t:str)-> bool:
        arr=[0] * 26

        for i in s:
            arr[ord(i) - ord('a')]+=1

        for i in t:
            arr[ord(i) - ord('a')]-=1

        for i in arr:
            if i > 0:
                return False

        return True


solution = Solution()
actual1 =solution.validAnagram("anagram","nagaram")
print(actual1)
actual2 =solution.validAnagram("anagram","nmgaram")
print(actual2)

