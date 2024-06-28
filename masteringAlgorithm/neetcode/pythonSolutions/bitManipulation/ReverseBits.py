
class Solution:
    def reverseBits(self, n: int) -> int:
        result =0;

        for i in range(32):
            bit = (n >> i) & 1
            print(bit)
            result = result | (bit << (31 - i))
            print("Result")
            print(result)

    def reverseBitsFourBits(self, n: int) -> int:
        result =0;

        for i in range(4):
            bit = (n >> i) & 1
            print(bit)
            result = result | (bit << (3 - i))
            print("Result")
            print(result)

solution = Solution()
solution.reverseBitsFourBits(1);
solution.reverseBitsFourBits(8);

solution = Solution()
solution.reverseBits(1);