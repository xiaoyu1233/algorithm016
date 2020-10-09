#回溯法

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index):
            if index == len(digits):
                res.append("".join(res_temp))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    res_temp.append(letter)
                    backtrack(index + 1)
                    res_temp.pop()
        res = []
        res_temp = []
        backtrack(0)
        return res