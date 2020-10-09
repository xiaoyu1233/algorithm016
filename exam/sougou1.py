from interval import Interval
class Solution:
    def solve(self, n, k, str1, str2):
        # write code here
        # return Interval(3,3)
        count = 0
        for i in range(n):
            if str1[i] == str2[i]:
                count += 1
        if count <= k:
            start = count - (n-k)
            end = count + (n-k)
        else:
            start = count
            end = k + (n-count)


        return Interval(start, end)
a = Interval()
a.start = 0
a.end = 5
return a