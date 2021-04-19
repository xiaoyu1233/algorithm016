#回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n: #终止条件，所有位置都被填满
                ans.append(''.join(S))
                return
            if left < n:    #如果左括号名额还有，填左括号，向下递归，撤回本步
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:    #如果右括号名额还有，填左括号，向下递归，撤回本步
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


# 动态规划
#光头哥的写法，非常简洁优美
class Solution:
    def generateParenthesis(self, n):
        def generate(p,left,right,parens=[]):
            if left: generate(p+'(',left-1,right)   #如果左括号名额还有，就加左括号，向下递归
            if right > left: generate(p+')',left,right-1)   #如果右括号名额还有，就加右括号，向下递归
            if not right: parens += p,  #如果右括号名额没有了，此时说明左括号名额也没有了，就将结果保存下来，不断保存知道所有递归结束返回结果
            return parens
        return generate('', n, n)