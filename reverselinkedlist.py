"""def reverselist(head):
    temp=head
    arr=[]
    while(temp):
        arr.append(temp.val)
        temp=temp.next
        arr=arr[::-1]
        i=0
        temp=head
        while(temp):
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head
    ==========================================="""



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

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Save next node
        current.next = prev       # Reverse current node's pointer
        prev = current            # Move prev up
        current = next_node       # Move current up
    return prev  # New head

# Example usage:
arr = [1, 2, 3, 4]
head = createlinkedlist(arr)

print("Original List:")
printlinkedlist(head)

head = reverseLinkedList(head)

print("Reversed List:")
printlinkedlist(head)

