# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def add_with_carry(val1, val2 , carry):
    helper = val1 + val2 + carry
    if helper >= 10:
        carry = math.floor(helper/10)
        helper = helper % 10
    else:
        carry = 0
    return helper, carry
        

class Solution: #using a class for this is weird and non-pythonic, but it was required on leetcode
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        root = True
        
        #will work if same size only lul
        #l3 = ListNode()
        
        while (l1 and l2):
            helper, carry = add_with_carry(l1.val, l2.val, carry)

            new_node = ListNode(helper)

            if root:
                l3 = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node

            l1 = l1.next
            l2 = l2.next
            root = False

        while (l1 and not l2):
            helper, carry = add_with_carry(l1.val, 0, carry)
            new_node = ListNode(helper)
            current_node.next = new_node
            current_node = new_node
            l1 = l1.next
            root = False

        while (l2 and not l1):
            helper, carry = add_with_carry(0, l2.val, carry)
            new_node = ListNode(helper)
            current_node.next = new_node
            current_node = new_node
            l2 = l2.next
            root = False

        if (carry != 0 and l1 == None and l2 == None):
            new_node = ListNode(carry)
            current_node.next = new_node
            #should be done here, no need to set current
            
        return l3
