#FizzBuzz题，按照逻辑写就好，在代码扩展性上可以做优化

#按逻辑写，先写重叠的情况，再计算其他的
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for num in range(1,n+1):

            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans



#子字符串，减少了判断次数
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1,n + 1):
            res_sub = ""
            if num % 3 == 0:
                res_sub += "Fizz"
            if num % 5 == 0:
                res_sub += "Buzz"
            if not res_sub:
                res_sub = str(num)
            res.append(res_sub)
        return res

#用映射做，扩展更自由
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}
        for num in range(1, n + 1):
            sub_res = ""
            for key in fizz_buzz_dict.keys():
                if num % key == 0:
                    sub_res += fizz_buzz_dict[key]
            if not sub_res:
                sub_res = str(num)
            res.append(sub_res)
        return res