#python又来秀了，一行到家
#两个思路，一个是基于堆的思想，堆天生适合找前k大的元素，一个是基于快排的思想


#python技巧
#直接使用Counter计数，直接取频数最大的几位
#collections.Counter(nums).most_common(k)代表取频数最大的k位，key和value打包成元组储存在列表中。
#*代表不确定几位，可有多位
#zip将对应位置元素打包成元组
#打包完后，第0个元素就是要求的，但是zip类型不能直接取，得先变成list，然后取第0位。
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(zip(*collections.Counter(nums).most_common(k)))[0]



#堆方法
#python维护的是最小堆。频数取反入队。先将所有数据的频数和它本身一起存到堆里。频数取反，这样每一次取到的都是最小值，也就是实际上的最大值。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

#桶排序，用频数作为桶的标签，往桶里放元素，从频数最大桶开始取，取到数量都k个,就是前k个最大元素。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        n = len(nums)
        c2 = [[] for _ in range(n + 1)]
        for v, c in counter.items():
            c2[c].append(v)
        res = []
        for i in range(n, -1, -1):
            res.extend(c2[i])
            if len(res) == k:
                return res

#快速排序
#分切分和找pivot两步走
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        val = list(counter.keys())
        l, r = 0, len(val) - 1
        while l <= r:
            pivot = self.partition(val, l, r, counter)
            if pivot == k - 1:  #刚好找到k个值，结束
                return val[:k]
            if pivot > k - 1:   #pivot比k大，说明查找空间还能缩减
                r = pivot - 1
            else:   #pivot比k小，说明查找空间在右边一点
                l = pivot + 1
#切分
    def partition(self, val, l, r, counter):
        #随机找一个值，防止pivot值固定，导致切分的两边差距太大pivot，并把pivot值换到最右边
        ran = random.randint(l, r)
        val[ran], val[r] = val[r], val[ran]

        #pivot是最右边的一个值，right指针记录比pivot大的值索引，往数组前面放
        pivot = r
        right = l
        for i in range(l, r):
            if counter.get(val[i]) >= counter.get(val[pivot]):  #遇到大于pivot的就向前放
                val[i], val[right] = val[right], val[i]
                right += 1  #记录有多少个比pivot大的
        val[right], val[pivot] = val[pivot], val[right] #将pivot放到所有比它大的值的后面
        return right    #返回pivot的位置索引







