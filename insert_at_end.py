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
    return head

def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

def insertAtEnd(head, data):
    new_node = node(data)   # Step 1: create new node
    if head is None:        # Step 2: if list empty, new node is head
        head = new_node
        return head
    temp = head
    while temp.next:        # Step 3: traverse till last node
        temp = temp.next
    temp.next = new_node    # Step 4: append new node at end
    return head

# Example usage:
arr = [1, 2, 3]
head = createlinkedlist(arr)

print("Before Insertion at end:")
printlinkedlist(head)

head = insertAtEnd(head, 4)

print("After Insertion at end:")
printlinkedlist(head)
