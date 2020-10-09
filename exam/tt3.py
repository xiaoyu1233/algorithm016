import sys
lines = int(input())
for line in sys.stdin:
    a = line.split()
    a.sort()
    c = ' ' .join(a)
    print(c)

    import collections


class Solution:
    def hashJoin(self, setA, setB):
        hashMap = {}
        sorted(setA)
        sorted(setB)
        for i in range(len(setA)):

            while setA[i] == setB[j] and j < len(setB) - 1:
                hashMap[i] = j
                j += 1
            while setA[i] > setB[j] and j < len(setB) - 1:
                j += 1
            while setA[i] < setB[j] and i < len(setA) - 1:
                i += 1
        print(hashMap)
        res = []
        for k, v in hashMap.items():
            subres = []
            subres.append(k)
            subres.append(v)
            res.append(subres)

        return res