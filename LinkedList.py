
## LINKEDLIST IMPLEMENTATION


# Node class for LinkedList
# This node contains two pointers : next and prev. 
# The data in the node is a key-value pair in order to represent the hash map. 

class Node:
    
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value 
        self.next = None
        self.prev = None 
    
    def disconnect(self):
        self.key = None
        self.value = None
        self.next = None
        self.prev = None 
        
        return

    def __repr__(self):
        return f"({self.key}, {self.value})"

class LinkedList:
    def __init__(self):
        #initialize a header and a trailer
        self.header = Node() 
        self.trailer = Node() 
        # link the two as a LinkedList
        self.header.next = self.trailer
        self.trailer.prev = self.header 
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def add(self, key, value):
      
        new_node = Node(key, value)
        # if this is a new(empty) Linkedlist

        if (self.is_empty()):
            self.header.next = new_node 
            self.trailer.prev = new_node
            new_node.prev = self.header
            new_node.next = self.trailer 
        
        else:
            # get the current last node
            new_node_prev = self.trailer.prev
            # set the new_node as the new last node 
            self.trailer.prev = new_node
            new_node.next = self.trailer 
            # connect the new node to the rest of the list 
            new_node_prev.next = new_node
            new_node.prev = new_node_prev
        
        self.size += 1

        return new_node 
    

    def get_node_with_key(self, key):
        curr_node = self.header.next
        while curr_node != self.trailer:
            if curr_node.key == key:
                return curr_node
            curr_node = curr_node.next 
        return None 


    def get_node_with_value(self, value):
        curr_node = self.header.next
        while curr_node != self.trailer:
            if curr_node.value == value:
                return curr_node
            curr_node = curr_node.next 
        return None


    def update (self, key, value):
        curr_node = self.get_node_with_key(key)
        if curr_node:
            curr_node.value = value 
            return curr_node 

    
    def delete (self, key):
        curr_node = self.get_node_with_key(key)
        if curr_node:
            curr_node.prev.next = curr_node.next 
            curr_node.next.prev = curr_node.prev 
            curr_node.disconnect()
            self.size -= 1   
        else:
            return None

    def __getitem__(self, key):
        return self.get_node_with_key(key) 
    
    def __iter__(self):
        curr_node = self.header.next 
        while (curr_node != self.trailer):
            yield (curr_node.key, curr_node.value)
            curr_node = curr_node.next 

    
    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"


ll1 = LinkedList()
