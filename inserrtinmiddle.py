def insertinmiddle(arr):
    if(head==None):
        return Node
    len=0
    temp=head
    while(temp):
        len+=1
        temp=temp.next
    if(len%2==0):
        prev=None
        slow=head
        fast=head
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        newnode=node(x)
        prev.next=newnode
        newnode.next=slow
        return head
    else:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        front=slow.next
        newnode=node(x)
        slow.next=newnode
        newnode.next=front
        return head














            
            
