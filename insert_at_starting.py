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

def insertAtBeginning(head, data):
    new_node = node(data)      # Create new node
    new_node.next = head       # Point new node to current head
    head = new_node            # Update head to new node
    return head

# Example usage:
arr = [2, 3, 4]
head = createlinkedlist(arr)
head = insertAtBeginning(head, 1)

printlinkedlist(head)
