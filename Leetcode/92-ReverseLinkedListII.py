from Leetcode.PalindromeLinkedList import current


class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseLinkedListII(head: [LinkedList], left, right):
    head_node = LinkedList(head[0])
    current = head_node
    for number in head[1:]:
        current.next = LinkedList(number)
        current = current.next

    



head = [1, 2, 3, 4, 5]
left = 2
right = 4
print(reverseLinkedListII(head, left, right))