class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseLinkedList(head: [LinkedList]):
        head_node = LinkedList(head[0])
        current = head_node
        for number in head[1:]:
            current.next = LinkedList(number)
            current = current.next

        node = None
        while current:
            temp = current.next
            current.next = node
            node = current
            current = temp
        return node

head = [1, 2, 3, 4, 5]
print(reverseLinkedList(head))