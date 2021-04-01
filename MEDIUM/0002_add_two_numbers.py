# 68 ms
# Linked List, Math, Recursion


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    ans = t = ListNode()
    carry = 0
    while(l1 and l2):
        s = l1.val + l2.val + carry     
        l1 = l1.next
        l2 = l2.next
        t.next = ListNode(s%10)
        carry = int(s/10)
        t = t.next
    
    l3 = l1 or l2
    while(l3):
        s = l3.val + carry
        l3 = l3.next
        t.next = ListNode(s%10)
        carry = s//10
        t = t.next
        if(not carry):
            t.next = l3
            return ans.next
        
    if(carry):
        t.next = ListNode(carry)
        
    return ans.next



"""  Another Solution """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    ans = t = ListNode()
    carry = 0
    while(l1 or l2):
        s = 0
        if(l1):
            s += l1.val
            l1 = l1.next
        if(l2):
            s += l2.val
            l2 = l2.next
        s += carry
        t.next = ListNode(s%10)
        t = t.next
        carry = s//10
        
    if(carry):
        t.next = ListNode(carry)
        
    return ans.next
