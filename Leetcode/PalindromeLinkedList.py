class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def palindromeLinkedList(head:[ListNode]):
    head_node = ListNode(head[0])
    current = head_node
    for element in head[1:]:
        current.next = ListNode(element)
        current = current.next
    print(head)

    if not current:
        return True

    fast = slow = head_node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        new_node = slow.next
        slow.next = prev
        prev = slow
        slow = new_node

#     checking for palindrome
    left, right = head_node, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


class Solution():
    # Helper to create a linked list from a list
    def create_linked_list(elements):
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head


head = [1,2,2,1]
print(palindromeLinkedList(head))



# Sesha's solution
# head_node = ListNode(head[0])
# current = head_node
# for i in range(1, len(head)):
#     new_node = ListNode(head[i])
#     current.next = new_node
#     current = new_node
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution():
#     def ispalindome(self, head: [ListNode]):
#         head_node = ListNode(head[0])
#         current = head_node
#         for i in range(1, len(head)):
#             new_node = ListNode(head[i])
#             current.next = new_node
#             current = new_node
#             prev = None
#             curr = head_node
#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
#         return prev

from poetry.console.commands import self class ListNode: def init(self, val=0, next=None): self.val = val self.next = next class Solution(): def ispalindome(self,head:[ListNode]): head_node = ListNode(head[0]) current = head_node for i in range(1, len(head)): new_node = ListNode(head[i]) current.next = new_node current = current.next slow = head_node fast = head_node while fast and fast.next: slow = slow.next fast = fast.next.next prev = None curr = slow while curr: next_node = curr.next curr.next = prev prev = curr curr = next_node #return prev.next left, right = head_node, prev # print(left.val) '''while left: print(left.val, end="," if left.next else "\n") left = left.next while right: print(right.val, end="," if right.next else "\n") right = right.next''' while left and right: if left.val != right.val: return False left = left.next right = right.next return True print(Solution.ispalindome(self,[1,3,2,1]))from poetry.console.commands import self class ListNode: def init(self, val=0, next=None): self.val = val self.next = next class Solution(): def ispalindome(self,head:[ListNode]): head_node = ListNode(head[0]) current = head_node for i in range(1, len(head)): new_node = ListNode(head[i]) current.next = new_node current = current.next slow = head_node fast = head_node while fast and fast.next: slow = slow.next fast = fast.next.next prev = None curr = slow while curr: next_node = curr.next curr.next = prev prev = curr curr = next_node #return prev.next left, right = head_node, prev # print(left.val) '''while left: print(left.val, end="," if left.next else "\n") left = left.next while right: print(right.val, end="," if right.next else "\n") right = right.next''' while left and right: if left.val != right.val: return False left = left.next right = right.next return True print(Solution.ispalindome(self,[1,3,2,1]))