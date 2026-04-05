def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    
    if head is None:
        return new_node
    
    cur = head
    
    while cur.next:
        cur = cur.next
    
    cur.next = new_node
    
    return head
