"""middlenode=getmiddle(head)
print(middlenode)
def getmiddle(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=fast.next
        fast=fast.next.next
    return slow

    ================================================================="""



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

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


arr = list(map(int, input("Enter values ").split()))
head = createlinkedlist(arr)# Create linked list and print it
mid = middleNode(head)# Find middle node
print(mid.val)# Print middle node value




