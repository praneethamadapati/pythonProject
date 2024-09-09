class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head:[ListNode]):
    head_node = ListNode(head[0])
    current = head_node
    for element in head[1:]:
        current.next = ListNode(element)
        current = current.next
    print(head)

    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    print(prev)
    return prev


head = [1, 2, 3, 4, 5]
print(reverseLinkedList(head))