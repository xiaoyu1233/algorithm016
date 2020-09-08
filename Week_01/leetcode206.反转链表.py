#方法一、递归
#超过97%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution():
    def reverseList(self,head):
        #如果列表为空或者列表已经到结尾，返回头结点
        def helper(pre,cur):
            if cur is None:
                return pre
            cur_next = cur.next
            cur.next = pre
            return helper(cur,cur_next)
        return helper(None,head)

#方法二、迭代
#超过91%
class Solution():
    def reverseList(self,head):
        #if head is None: return
        pre, cur = None, head
        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        return pre

