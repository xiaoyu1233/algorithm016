#题目要求就是删除每个大括号单元的最外层括号，原语化理解老半天
#主要是两个思路，一个是计数，一个是栈。这道的局部相关性很强，拿到就应该想到借助栈结构实现。存储结果的时候避开第一个入栈和最后一个出栈的元素就好。

#双指针计数
#超58%
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        '''
        1. 原语化。2. 拆除各原语最外层括号。
        双指针查找各原语下标
        (()())()
        12121010
        '''
        # 双指针 寻找原语化的最外层括号下表
        primitive_indices = []
        left, count = 0, 0
        for i in range(len(S)):
            if S[i] == "(": count += 1
            elif S[i] == ")": count -= 1
            if count == 0:                        # 找到最外层右括号
                primitive_indices.append((left, i))  # 添加答案
                left = i + 1                         # 更新最外层左括号指针
        # 根据下标，提取原语，切片拆除括号
        return "".join( S[m+1:n] for m, n in primitive_indices )

#单指针计数，边走边存
#超58%
class Solution:
    def removeOuterParentheses(self, S):
        res, count = [], 0
        for c in S:
            if c == '(' and count > 0: res.append(c)
            if c == ')' and count > 1: res.append(c)
            count += 1 if c == '(' else -1
        return "".join(res)



#栈方法
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        '''
        借助栈来判断，把非外层括号放进答案中。
        '''
        res, stack = "", []
        for c in S:
            # 什么情况下，某个括号要加入结果中呢？非外层括号。
            # 怎么判断是非外层括号？ 1. 左括号加入前，栈不为空。避开第一个左括号。2. 右括号加入并消括号后，栈不为空，避开最后一个右括号。
            if c == "(":
                if stack: res += c
                stack.append("(")
            if c == ")":
                stack.pop()
                if stack: res += c
        return res

