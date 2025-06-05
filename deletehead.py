# Node definition for singly linked list
class node:
    def __init__(self, data):
        self.val = data
        self.next = None

# Function to create a linked list from a list of values
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

# Function to print the linked list
def printlinkedlist(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

# Function to delete the head of the linked list
def deletehead(head):
    if head is None:
        return None  # List is empty
    front = head.next  # Move head to next node
    head.next = None   # Disconnect the old head
    return front       # Return the new head

# ✅ Example usage
arr = [10, 20, 30]
head = createlinkedlist(arr)

print("Original List:")
printlinkedlist(head)

head = deletehead(head)  # Delete the head node

print("After Deleting Head:")
printlinkedlist(head)
