class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=0xFFFFFF
        MAX=0xFFFFFF

        while b !=0:
            sum_without_carry= (a ^ b) & MASK
            carry = ((a & b) << 1 ) & MASK

            a , b = sum_without_carry, carry

        if a > MAX//2:
            return ~(a ^ MASK)
        return a

solution = Solution()
actual1 = solution.getSum(2,3)
print(actual1)

actual2 = solution.getSum(2,1)
print(actual2)