#python技巧
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = [i*10**index for index,i in enumerate(digits[::-1])]
        nums += 1
        return [int(x) for x in str(nums)]


# python技巧
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0,1)
                    return digits


