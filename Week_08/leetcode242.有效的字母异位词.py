#python炫技题，排序和哈希两种方法，都可以一行解决
#人生苦短，我用python,不好意思，先行一步了

#哈希
#超96%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

#排序
#超6%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

