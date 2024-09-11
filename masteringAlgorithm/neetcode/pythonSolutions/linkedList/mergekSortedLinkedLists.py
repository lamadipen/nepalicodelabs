import json
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList =[]
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None

                mergedList.append(self.mergeTwoList(l1,l2))
            lists = mergedList

        return lists[0]

    def mergeTwoList(self, l1,l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


solution = Solution()
l3 = ListNode(4)
l2 = ListNode(2,l3)
l1 = ListNode(1,l2)


s3 = ListNode(5)
s2 = ListNode(3,s3)
s1 = ListNode(1,s2)

t2 = ListNode(6)
t1 = ListNode(3,t2)

actual1 = solution.mergeKLists([l1,s1,t1])
json.dumps(actual1,  default=vars)
print(json.dumps(actual1,  default=vars) == '{"val": 1, "next": {"val": 1, "next": {"val": 2, "next": {"val": 3, "next": {"val": 3, "next": {"val": 4, "next": {"val": 5, "next": {"val": 6, "next": null}}}}}}}}')