#两数之和，有两种方法，一种是排序后遍历，一种是哈希表方法。这里只写哈希方法。
#这道题巧妙地利用了哈希方法，避开了两个相同数。虽然两个相同的数会产生哈希冲突，但并不会影响结果的正确性。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if hashMap.get(target-nums[i]) is not None:
                return [hashMap.get(target-nums[i]),i]
            hashMap[nums[i]] = i