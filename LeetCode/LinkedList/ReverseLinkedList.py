'''
        Given the head of a singly linked list, reverse the list, and return the reversed list.

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Example 2:
        Input: head = [1,2]
        Output: [2,1]

        Example 3:
        Input: head = [1]
        Output: [1]
 

        Constraints:

        The number of nodes in the list is the range [0, 5000].
        -5000 <= Node.val <= 5000
 

        Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?   
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# # Approach iterative
# def reverseList( head: ListNode) -> ListNode:
#     prev = None
#     current = head

#     while current:
#         next_node = current.next  # Save the next node
#         current.next = prev       # Reverse the link
#         prev = current            # Move 'prev' forward
#         current = next_node       # Move 'current' forward

#     return prev  # New head of the reversed list

# Approach : recursive
def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head  # Base case: if list is empty or contains one node

    new_head = reverseList(head.next)  # Recursively reverse the rest of the list
    head.next.next = head  # Point next node back to the current node
    head.next = None       # Break the forward link

    return new_head  # Return the new head



# Execution:
def print_linked_list(head: ListNode):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_list = reverseList(head)
print_linked_list(reversed_list)  # Output: 5 -> 4 -> 3 -> 2 -> 1
