#两种做法，一种是动态规划，一种是小顶堆。
#第i个丑数和前面的丑数有联系，所以想到动态规划
#求的是第i个小的丑数，这类问题常用堆，所以想到堆


#动态规划
#第i个丑数肯定是由之前的丑数乘以2、3、5得到的，并且是之前已出现的丑数乘以2、3、5后的最小值
#因此我们记录之前得到的丑数，对于每个丑数，只有一次乘2、3、5的机会，乘过了之后就计算下一个丑数。
#超73%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1  #注意这里是if而不是elif,要排除重复解
            if dp[i] == n5: c += 1
        return dp[-1]



#小顶堆
#超22%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = set()    #记录见过的丑数，防止重复解
        seen.add(1)
        factors = [2,3,5]

        for _ in range(n):
            cur_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = cur_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly
