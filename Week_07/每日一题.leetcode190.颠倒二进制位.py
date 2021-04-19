class Solution:
    def reverseBits(self, n: int) -> int:
        #print(bin(n))
        return int(bin(n)[2::].zfill(32)[::-1], base=2)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

#https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode/
#还有位操作部分没有看完