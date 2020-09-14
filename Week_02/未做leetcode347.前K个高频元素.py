#python又来秀了，一行到家
#两个思路，一个是基于堆的思想，堆天生适合找前k大的元素，一个是基于快排的思想
#
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
#python维护的是最小堆。求最小的k个数时维护大小为k的最大堆，这样就可以得到小于等于堆顶的k个数
#求最大的k个数，维护大小为k的最小堆，这样就可以得到大于等于堆顶的k个数
#python内置的是最小堆，所以这里我们将数值取反，求最大的k个数
#超80%
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)   #建堆，使列表具有堆的性质
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]: #是我们想要得到的数，入堆
                heapq.heappop(hp)   #弹出堆顶
                heapq.heappush(hp,-arr[i])    #入堆
        ans = [-x for x in hp]
        return ans





