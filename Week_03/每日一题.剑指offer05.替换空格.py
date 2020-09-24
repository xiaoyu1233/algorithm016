#python技巧
#replace方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

#python技巧
#split方法+join方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        return '%20'.join(s.split(' '))

#由于python中字符串是不可变类型，因此重开数组不可避免。
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == ' ':
                res.append('%20')
            else:
                res.append(ch)
        return "".join(res)
