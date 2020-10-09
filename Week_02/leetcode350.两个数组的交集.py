#python炫技题，排序和哈希两种方法
#人生苦短，我用python,不好意思，先行一步了

#哈希
#超63%
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2   #key取交，value取小
        return list(num.elements())


#光头哥的简洁写法
#超80%
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1, num2 = map(collections.Counter, (nums1, nums2))
        return list((num1 & num2).elements())

#python不使用Counter时的哈希写法
#超80%
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.defaultdict(int)
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            if (m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection
#排序
#超46%
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)
        intersection = []
        index1, index2 = 0, 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        return intersection


