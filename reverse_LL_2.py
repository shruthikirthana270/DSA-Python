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

# Function to reverse from left to right
def reverse_between(head, left, right):
    if left == right:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Move prev to node before 'left'
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next




# Example use
lst = [1, 2, 3, 4, 5]
left = 2
right = 4

head = createlinkedlist(arr)
print("Original list:")
print_list(head)

head = reverse_between(head, left, right)
print("Reversed list (from position", left, "to", right, "):")
print_list(head)
