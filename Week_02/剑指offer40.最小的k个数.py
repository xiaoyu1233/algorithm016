
#python技巧
#超80%
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

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





