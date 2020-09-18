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






