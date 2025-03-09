'''
        Given the head of a singly linked list, group all the nodes with odd indices 
        together followed by the nodes with even indices, and return the reordered list.

        The first node is considered odd, and the second node is even, and so on.
        Note that the relative order inside both the even and odd groups should remain as 
        it was in the input.

        You must solve the problem in O(1) extra space complexity and O(n) time complexity.
    

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [1,3,5,2,4]

        Example 2:
        Input: head = [2,1,3,5,6,4,7]
        Output: [2,3,6,7,1,5,4]

        Constraints:
        The number of nodes in the linked list is in the range [0, 104].
        -106 <= Node.val <= 106    
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    
    odd.next = even_head  # Append the even list to the odd list
    return head

# Execution
def print_linked_list(head):
    while head:
        print(head.val, end=" , " if head.next else "\n")
        head = head.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = oddEvenList(head)
print_linked_list(result)  # Output: 1 , 3 , 5 , 2 , 4
