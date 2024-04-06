class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        last_node = self.head.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                last_node = self.head.prev
                self.head = self.head.next
                last_node.next = self.head
                self.head.prev = last_node
            return
        current_node = self.head.next
        while current_node != self.head:
            if current_node.data == key:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while True:
            print(current_node.data, end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print()
    
    def search(self, value):
        startpoint = self.head
        stopper = self.head
        while True:
            if stopper.data == value:
                return stopper
            stopper = stopper.next

            if startpoint.data == stopper.data and startpoint.prev.data == stopper.prev.data and startpoint.next.data == stopper.next.data:
                raise SearchFailed("Value does not exist, whole list traveled.")

class SearchFailed(Exception):
    pass

# create Circular Doubly Linked List
def createCDLL(array):
    dllist = DoublyLinkedList()
    for i in array:
        dllist.append(i)
    return dllist