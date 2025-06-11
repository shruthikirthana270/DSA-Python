class node:
    def __init__(self, data):
        self.val = data
        self.next = None

def createlinkedlist(arr):
    head = None 
    for data in arr:
        if head is None:
            head = node(data)
            temp = head
        else:
            temp.next = node(data)  
            temp = temp.next
    printlinkedlist(head)
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Example usage:
arr = [1, 2,3]
head = createlinkedlist(arr)
"""tail = head
while tail.next:
    tail = tail.next
tail.next = head.next.next """

print("Cycle detected?", hasCycle(head))
