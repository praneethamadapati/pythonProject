class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    @staticmethod
    def linkedListCycle(head: LinkedList):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False

def create_linked_list(elements, pos):
    """ Helper function to create a linked list with an optional cycle.
    :param elements: List of elements to include in the LinkedList.
    :param pos: Position at which the cycle should begin; -1 if no cycle.
    :return: The head of the linked list.
    """
    head = LinkedList(elements[0])
    current = head
    cycle_start = None

    for index in range(1, len(elements)):
        current.next = LinkedList(elements[index])
        current = current.next
        if index == pos:
            cycle_start = current

    if pos != -1:  # Create cycle
        current.next = cycle_start

    return head

# Creating a linked list: 3 -> 2 -> 0 -> -4 (links back to 2)
head = create_linked_list([3, 2, 0, -4], 1)

# Checking if there is a cycle
print(Solution.linkedListCycle(head))  # Expected: True