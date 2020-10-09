#递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        return self.reversePrint(head.next) + [head.val]

#辅助栈
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []

        while head:
            val = head.val

            stack.append(val)
            head = head.next
        return stack[::-1]