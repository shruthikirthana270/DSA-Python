class node:
    def __init__(self, data):
        self.val = data
        self.next = None

def createlinkedlist(arr):
    head = None 
    for data in arr:
        if (head == None):
            head = node(data)
            temp = head
        else:
            temp.next = node(data)  
            temp = temp.next
    printlinkedlist(head)
    return head

def printlinkedlist(head):
    temp=head
    while(temp):
        print(temp.val,end=" ")
        temp=temp.next
arr = list(map(int, input().split()))
createlinkedlist(arr)
