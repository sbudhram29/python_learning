class Node:
    """
    An object for storing a single node of a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    def __init__(self, head):
        if(type(head) != Node):
            self.head = Node(head)
        else:
            self.head = head

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return length of List
        Take O(n)
        """
        count = 1
        current = self.head
        while current.next != None:
            count += 1
            current = current.next
        return count

    def add(self, data):
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = Node(data)

    def delete(self, data):
        current = self.head

        if current.data == data:
            self.head = current.next
            return None

        while current.next != None:
            if data == current.next.data:
                current.next = current.next.next
                return None
            current = current.next


node_list = LinkedList(1)
node_list.add(2)

print(node_list.size())
node_list.delete(2)
print(node_list.size())
node_list.delete(2)
print(node_list.size())
