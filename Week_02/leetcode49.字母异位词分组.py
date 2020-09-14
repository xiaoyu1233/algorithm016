#有两种思路，一个是将字符串打散成一个排序的字符数组（python中用sorted直接实现），然后将这个排序数组（转换成元组），作为字典的键，不断向内田间打散后等于这个键的值。
#一种是将组成字符串的26个字母统计计数作为字典的键值，相当于用26个数编码这个字符串，编码相同的就是字母异位词。
#python在这两种方法上都展示了强大的技巧性。
#python技巧
#超76%
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s) #python字典的键只接受数字、字符串、元组这些不可变类型。
        return list(ans.values())   #输出不能是字典值类型，直接用list转化下

#defaultdict(list)的用处是当字典中不存在这个键的时候，返回[]。如果不使用defaultdict，要防止键不存在时访问发生错误，还可以用get(key,[])来设定默认返回值为[]
#超61%
class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())


#python技巧
#超61%
class Solution:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


