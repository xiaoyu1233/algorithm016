#贪心
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g,reverse=True)
        s = sorted(s,reverse=True)
        i = j = count = 0
        while i != len(g) and j != len(s):
            if g[i] <= s[j]:
                j += 1
                count += 1
            i += 1
        return count