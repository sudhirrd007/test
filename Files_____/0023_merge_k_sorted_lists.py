"""
url : https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertLast(self, val):
        self.last.next = ListNode(val)
        self.last = self.last.next

    def insertFirst(self, val):
        node = ListNode(val)
        node.next = self.main
        self.main = node
        
    def insert(self, val):
        current = self.main             
        previous = self.main
        while(val > current.val):
            previous = current
            current = current.next
        previous.next = ListNode(val)
        previous.next.next = current

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        flag = True
        self.main = None
        for i in lists:
            if(i):
                if(flag):
                    self.main = i
                    current = self.main
                    self.last = current
                    while(current):
                        self.last = current
                        current = current.next
                    high = self.last.val
                    low = self.main.val
                    flag = False
                else:
                    if(i.val >= high):
                        self.last.next = i
                        current = self.last
                        while(current):
                            self.last = current
                            current = current.next
                        high = self.last.val
                        continue
                    while(i):
                        if(i.val >= high):
                            self.insertLast(i.val)
                            high = i.val
                        elif(i.val <= low):
                            self.insertFirst(i.val)
                            low = i.val
                        else:
                            self.insert(i.val)
                        i = i.next
        if(not self.main):
            return ListNode(0).next
        return self.main

" FAST --------------------------------------------------------- "
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def myFunc(val):
            return val[0]
        self.nodes = []
        for l in lists:
            while l:
                self.nodes.append([l.val, l])
                l = l.next
                
        self.nodes.sort(key=myFunc)
        
        for index, (val,l) in enumerate(self.nodes[:-1]):
            l.next = self.nodes[index+1][1]
            
        if(self.nodes):
            return self.nodes[0][1]
        else:
            return ListNode(0).next