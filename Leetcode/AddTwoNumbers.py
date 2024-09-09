class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers( l1: [2, 4, 3], l2: [5, 6, 4]) -> [ListNode]:
        dummy_node = ListNode(0)
        current = dummy_node
        carry = 0

        while l1 or l2 or carry:
            value1 = (l1.val if l1 else 0)
            value2 = (l2.val if l2 else 0)
            carry, out = divmod(value1 + value2 + carry, 10)

            current.next = ListNode(out)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_node.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
Solution.addTwoNumbers(l1, l2)
