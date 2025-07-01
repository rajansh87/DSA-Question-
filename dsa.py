# Question 1: Merge k Sorted Lists 
# You are given an array of k linkedlist heads, each list being sorted in ascending order. Write a function to merge all the lists into one sorted linked list and return its head. 

# Example: 

# Input: lists = [[1->4->5],[1->3->4],[2->6]] 

# Output: 1->1->2->3->4->4->5->6 

# Explanation: The merged linked list in ascending order. 

class Node:# linked list node ds.
    def __init__(self,data):
        self.data = data
        self.next = None
        
def merge_sorted_ll(head1,head2):
    start = head1
    start2 = head1
    final_head = Node(-1)
    temp = final_head
    while head1 and head2:
        if head1.data < head2.data:
            final_head.next = head1
            head1 = head1.next
        else:
            final_head.next = head2
            head2 = head2.next
        final_head = final_head.next
    while head1:
        final_head.next = head1
        head1 = head1.next
        final_head = final_head.next
    while head2:
        final_head.next = head2
        head2 = head2.next
        final_head = final_head.next
    return temp.next
    
def solve(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    head = Node(-1)
    
    while len(arr)>1:
        head1 = arr.pop(0)
        head2 = arr.pop(0)
        head3 = merge_sorted_ll(head1,head2)
        arr.append(head3)
        
    return arr[0]

def printLL(head):
    print("Output")
    while head:
        print(head.data)
        head = head.next


    
head1 = Node(1)
head1.next = Node(4)
head1.next.next = Node(5)

head2 = Node(1)
head2.next = Node(3)
head2.next.next = Node(4)

head3 = Node(2)
head3.next = Node(6)

arr = [head1,head2,head3]
ans = solve(arr)
printLL(ans)
