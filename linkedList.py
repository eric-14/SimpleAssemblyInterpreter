class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    
    def add_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(index-1):
                if current_node.next is None:
                    raise IndexError("Index out of bounds")
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
    
    def sort(self):
        if not self.head:
            return
        swapped = True
        while swapped:
            swapped = False
            current_node = self.head
            while current_node.next:
                if current_node.data > current_node.next.data:
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                    swapped = True
                current_node = current_node.next
                    
    def __str__(self):
        current_node = self.head
        str_list = []
        while current_node:
            str_list.append(str(current_node.data))
            current_node = current_node.next
        return "->".join(str_list)
