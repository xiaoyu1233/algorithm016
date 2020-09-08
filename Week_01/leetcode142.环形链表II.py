#方法一、快慢指针,Floyed方法
#超过68%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersect(self, head):
        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        hare = self.getIntersect(head)
        tortoise = head
        if not hare: return None
        while tortoise:
            if tortoise == hare:
                return tortoise
            tortoise = tortoise.next
            hare = hare.next

#方法二、哈希
#超过68%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hashMap = {}
        while head:
            if hashMap.get(head) is not None:
                return head
            hashMap[head] = 1
            head = head.next
        return None



