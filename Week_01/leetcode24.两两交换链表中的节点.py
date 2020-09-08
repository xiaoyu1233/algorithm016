#方法一、递归
#超过91%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 如果列表为空或者列表已经到结尾，返回头结点
        if not head or not head.next:
            return head
        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

#方法二、迭代
#超过75%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            # 注意次序，别形成环
            pre_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            pre_node = first_node
            head = first_node.next
        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None



