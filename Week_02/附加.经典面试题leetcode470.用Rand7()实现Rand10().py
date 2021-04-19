'''
用Rand10生成Rand7很好做，只要超过7的值拒绝掉就好，可以保证生成的值在1-7之间是等概率的。
用Rand7生成Rand10，一个Rand无法铺满10的空间，所以要用两个骰子，两个7如果直接叠加，生成的空间是2-14，并且每个值不是等概率的。
那么如何用两个骰子均匀铺满整个空间，这样铺，(rand7()-1)*7+rand7(),一个骰子控制尺度，一个骰子控制位移，两个骰子分别负责不同的部分，
保证了1-49间每一个数都是等概率生成的。
现在我们等概率地生成1-49间的每一个数，那么我们可以直接取前10个数，拒绝其余数就可得到等概率的1-10。
但是这样比较慢，因为我们只使用了10/49的数，可以将40个数映射到10个数，这样我们的效率就可以得到提升。
再进一步地，我们现在还得到了1-9的等概率映射，现在我们要将浪费掉的Rand9也利用起来，用rand9去控制尺度，(rand9()-1)*7+rand7()铺满空间，
得到1-63的随机数，1-60映射到1-10，剩下3个数，Rand3也利用起来，(rand3()-1)*7+rand7()，生成1-21的随机数，剩下1无法利用了。OK提升到头了。
'''
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

#基本解法
#超5%
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()
        while num > 10:
            num = (rand7() - 1) * 7 + rand7()
        return num


#一级优化
#超50%
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        num = (rand7() - 1) * 7 + rand7()
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return 1 + num % 10 #因为取余操作不会取到10，所以数字+1平移，平移后依然是等概率

#二级优化
#超87%
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # num = (rand7() - 1) * 7 + rand7()
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40: return 1 + num % 10
            num = (num - 40 - 1) * 7 + rand7()
            if num <= 60: return 1 + num % 10
            num = (num - 60 - 1) * 7 + rand7()
            if num <= 20: return 1 + num % 10

        return 1 + num % 10  # 因为取余操作不会取到10，所以数字+1平移，平移后依然是等概率

