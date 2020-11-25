#排序，每次贪心地选择前k多的任务进行安排

#堆，与排序思想相同，但使用堆方法来取前k多的任务

#桶方法
#将每个任务冷却时间视为一个桶，向桶中放任务。
#分两种情况讨论，一种是任务的种类比较少，桶都没有放满。
#此时的时间长度为（桶的个数-1）X桶的大小+最后一个桶中任务的数量。此时等待时间是客观存在的，不得不等。
#一种是任务种类很多，桶都装满溢出了，那么时间就直接是任务数量，此时没有等待时间，必然是最优时间。我们要做的优化就是使等待时间最短。
#那么存不存在有些桶装满了，有些桶装不满的情况呢？
#答案是不存在。如果前面的桶装满了，后面的桶没装满，根据题意每个桶里的任务都是互不相同的，那么将前面溢出来的任务装到后面不满的桶中即可。
'''
假设时间间隔为3，则设桶的容量为4，桶的数量不限

桶1：A   B   D   F
桶2：A   B   D   F
桶3：A   C   E   
桶4: A   C   E
桶5：A      

填不满的部分是必然要等的时间，这部分时间不得不等。
'''




#一直装到所有桶都满了，或者到最后也没装满所有的桶，最终就变成了上面的两种情况。两种情况取最大值，就是所需的最少时间。


#桶方法，python库
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))
#桶方法，手写哈希
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        Hash = {}
        for i in tasks:
            Hash[i] = Hash.get(i, 0) + 1

        task_max = max(Hash.values())
        residual = 0
        for key in Hash.keys():
            if Hash[key] == task_max:
                residual += 1
        res = (task_max-1) * (n+1) + residual

        return res if res >= len(tasks) else len(tasks)

