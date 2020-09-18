#字符化做法，将数字字化，这样方便取到每一位的值。
class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)  #字符化num，这样方便取到各个位置的值
        while len(str_num) > 1:
            temp_num = 0    #各个位置相加的值保存在这儿，每次开始前初始化
            for i in range(len(str_num)):
                temp_num += int(str_num[i]) #各个位置相加
            str_num = str(temp_num) #替换原来做运算的值，字符化
        return int(str_num) #输出是个数字，转换成int

#更简洁的写法，用map直接映射变量类型，判断数字是否超过10
def addDigits(self, num: int) -> int:
    while num >= 10:
        digit = list(map(int, str(num)))
        #因为我不想再用一个变量接结果我就把num先置零，以防历史值影响计算
        num = 0
        for i in range(len(digit)):
            num += digit[i]
    return num


#模10取每一位数字的解法
def addDigits3(self, num: int) -> int:
    while num >= 10:
        sub_sum = 0
        while num > 0:
            sub_sum += num % 10
            num //= 10
        num = sub_sum
    return num

'''
#数学规律
xyz = 100x + 10y + z = 99x + 99y + (x+y+z)
x，y，z的最大值可能都是9，所以（x+y+z）之和可能是两位数也可能是一位数。如果是一位数正好就是我们模9的余数，如果是两位数则又变成了
mn = 10m + n = 9m + (m+n)，m+n存在1+9的情况是两位数，可以继续分解成9的倍数，其余均为1位数可以输出了。
因此xyz被9取余后，剩下的余数就是要求的值。
'''
def addDigits(self, num: int) -> int:
    if (num % 9 == 0) and (num != 0):
        return 9
    else:
        return num % 9

