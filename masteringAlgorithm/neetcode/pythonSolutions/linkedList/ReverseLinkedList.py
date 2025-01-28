#Reverse Linked List
# https://neetcode.io/problems/reverse-a-linked-list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def buildLinkedList(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for item in arr[1::]:
            current.next = ListNode(item)
            current = current.next

        return head

    def printLinkedList(self, head):
        if not head:
            print('Empty List')

        while head:
            print(str(head.val) , end=" -> ")
            head = head.next
        print('None')

    def reverseListStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        dummy = ListNode()
        current = dummy

        while stack:
            node = stack.pop()
            node.next = None
            current.next = node
            current = current.next

        return dummy.next

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return  None

        newHead = head

        if  head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead

    def reverseListEffieient(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next= prev
            prev = curr
            curr = temp

        return prev




solution = Solution()
#itrerative
linkList1 = solution.buildLinkedList([0,1,2,3])
solution.printLinkedList(linkList1)
reversedLinkList1 = solution.reverseListStack(linkList1)
solution.printLinkedList(reversedLinkList1)
linkList1 = solution.buildLinkedList([])
solution.printLinkedList(linkList1)
reversedLinkList1 = solution.reverseListStack(linkList1)
solution.printLinkedList(reversedLinkList1)


#recursive
print('recursive')
linkList1 = solution.buildLinkedList([0,1,2,3])
solution.printLinkedList(linkList1)
reversedLinkList1 = solution.reverseListRecursive(linkList1)
solution.printLinkedList(reversedLinkList1)
linkList1 = solution.buildLinkedList([])
solution.printLinkedList(linkList1)
reversedLinkList1 = solution.reverseListRecursive(linkList1)
solution.printLinkedList(reversedLinkList1)



