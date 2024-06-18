#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

class Solution:

    # Runtime O(n)
    # Space Complexity O(n)
    def removeNthNodeFromEndOfListSetImpl(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack =[]
        current = head

        while current:
            stack.append(current)
            current = current.next

        while stack and n > 0:
            stack.pop()
            n-=1

        if stack:
            stop = stack.pop()
            stop.next = stop.next.next
        else:
            return None

        return head

    def removeNthNodeFromEndOfList(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(-1, head)
        left=dummy
        right=head

        while n > 0:
            right=right.next
            n-=1

        while right:
            left=left.next
            right=right.next

        left.next = left.next.next

        return dummy.next


def buildLinkedList(input):
    dummy = ListNode()
    current = dummy
    for i in input:
        current.next = ListNode(i)
        current = current.next
    return  dummy.next

def printLinkedList(head:Optional[ListNode]):
    if not head:
        print("None")
    while head:
        print(head.val,end="->")
        head=head.next
    print('')

solution = Solution()
input1=buildLinkedList([1,2,3,4,5])
actual1 = solution.removeNthNodeFromEndOfListSetImpl(input1,2)
printLinkedList(actual1)
input2=buildLinkedList([1])
actual2 = solution.removeNthNodeFromEndOfListSetImpl(input2,1)
printLinkedList(actual2)
input3=buildLinkedList([1,2])
actual3 = solution.removeNthNodeFromEndOfListSetImpl(input2,1)
printLinkedList(actual3)

input4=buildLinkedList([1,2,3,4,5])
actual4 = solution.removeNthNodeFromEndOfList(input1,2)
printLinkedList(actual4)
input5=buildLinkedList([1])
actual5 = solution.removeNthNodeFromEndOfList(input2,1)
printLinkedList(actual5)
input6=buildLinkedList([1,2])
actual6 = solution.removeNthNodeFromEndOfList(input2,1)
printLinkedList(actual6)