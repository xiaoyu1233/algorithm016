#按照逻辑写就行，考熟练度和细节吧
#超过87%
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next  # 定个锚点，这k个链结束的地方就是pre
        temp = head  # 现在的头要变成翻转后的尾巴，存一下
        while pre != tail:
            temp_next = temp.next   #别忘了写next,会死循环的
            temp.next = pre
            pre = temp
            temp = temp_next
        return tail, head  # 得到新的头尾节点

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre  # 找k链的尾结点
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next  # 不满k个，就直接是返回哑结点。
            # 把翻转后的链连接到总链上去
            temp_next = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = temp_next
            pre = tail
            head = tail.next
        return dummy.next
