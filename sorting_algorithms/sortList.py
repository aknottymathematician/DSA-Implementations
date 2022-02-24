'''
Given the head of a linked list, return the list after sorting it in ascending order.
'''

'''
We will solve this using Merge Sort. So Time Complexity will O(NlogN) and Space Complexity will be O(N)
General Algorithm to sort using Merge Sort is -
1. Split the list into two parts.
2. Compare the elements once we reach the Base Case.
3. Merge the list with the sorted values.

> The only difference for us will be in this for problem we will be applying Merge Sort on a Linked List.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        # if list if empty or catains just one element
        if not head or not head.next:
            return head
        
        #Split the list
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)


    def getMid(self,head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        tail = dummy = ListNode()

        while left and right:
            if left.val<right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next
        
        if left:
            tail.next = left
        
        if right:
            tail.next = right
        
        return dummy.next


arr = [4,2,1,3]
sol = Solution()
print(sol.sortList(arr))