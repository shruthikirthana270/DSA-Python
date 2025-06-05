class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def createLinkedList(arr):
    head = None
    for data in arr:
        if head is None:
            head = Node(data)
            temp = head
        else:
            temp.next = Node(data)
            temp = temp.next
    return head

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()

def deleteTail(head):
    if head is None or head.next is None:
        return None  # Only 0 or 1 node exists

    temp = head
    while temp.next.next:  # Traverse to second last node
        temp = temp.next

    temp.next = None  # Remove last node
    return head
arr = [1, 2, 3]
head = createLinkedList(arr)

head = deleteTail(head)
printLinkedList(head)






















