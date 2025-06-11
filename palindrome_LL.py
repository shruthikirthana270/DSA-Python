class node:
    def __init__(self, data):
        self.val = data
        self.next = None
def createlinkedlist(arr): #fun def
    head = None
    for data in arr:
        if (head == None):
            head = node(data)
            temp = head
        else:
            temp.next = node(data)
            temp = temp.next
    return head
def printlinkedlist(head):#fun def
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()
def isPalindrome(head):
    values = []
    temp = head
    while temp:
        values.append(temp.val)
        temp = temp.next
    return values == values[::-1]
arr = [1, 2, 2, 1]
head = createlinkedlist(arr)#fun call
printlinkedlist(head)#fun call
if isPalindrome(head):
    print("palindrome.")
else:
    print("not a palindrome.")
