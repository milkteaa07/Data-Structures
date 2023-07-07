#!/usr/bin/env/python3

"""
atds.py
a compilation of useful classes...

Advanced Topics Data Structures
A collection of data structures learned in the Advanced Topics in Computer Science course
"""

__author__ = "Ava Teng"
__version__ = "2023-02-17"


class Stack(object):
    def __init__(self):
        self.stack = []
    
    def get_stack(self):
        return self.stack
        
    def size(self):
        return len(self.stack)   
     
    def push(self, item):
        # Adds an item to the end of the list, ie. the top of the stack.
        self.stack.append(item)
        
    def pop(self):
        # removes the last item on the list, ie. the top of the stack
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def __repr__(self):
        return  str(self.stack)
     
class Queue(object):
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __repr__(self):
        return "Queue" + str(self.queue)
        
class Deque(object):
    # front = start of list, rear = end of list
    def __init__(self):
        self.queue = []
        
    def get_queue(self):
        return self.queue
    
    def size(self):
        return len(self.queue)
    
    def add_front(self, item):
        self.queue.insert(0, item)
        
    def add_rear(self, item):
        self.queue.append(item)
        
    def remove_front(self):
        del self.queue[0]
        
    def remove_rear(self):
        del self.queue[-1]
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        string = ''
        for i in range(len(self.queue)):
            string += str(i+1) + " " + str(self.queue[i]) + '\n'
        return "QUEUE: \n" + string
    
class Node(object): 
    "Creates a Node object with a payload and a pointer."
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

    
    def __repr__(self):
        return "Node[data = " + str(self.data) + \
            ", next = " + str(self.next) + "]"
        
class UnorderedList(object):
    def __init__(self):
        self.head = None
        
    def add(self, item):
        #allows us to add an item to the beginning of the list. 
        #(For the moment, we're going to assume it's a unique item, and that it's not already present on the list.)
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
        
    def length(self):
        #returns the number of items in the list.
        """Traverses the list to identify how many nodes we have"""
        node_count = 0 
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count
    
    def remove(self, data): 
        #removes the specified item from the list. This assumes that the item is already in the list.
        previous = None                
        current = self.head         
        while current != None:              
            if current.get_data() == data:   
                current.set_data("")
                if previous == None:        
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())      
            else:
                previous = current            
                current = current.get_next()
                
    def search(self, item):
        #looks for the specified item in the list, and returns True it if is there somewhere.
        current = self.head

        while current != None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
                
    def append(self, item):
        #adds the item to the end of the list.
        new_node = Node(item)
        current = self.head
        while current != None:
            if current.get_next() == None:
                current.set_next(new_node)
                break
            else:
                current = current.get_next()
        
    def index(self, item):
        #returns the position of the item in the list (and assumes it is in the list)
        pos = 0 
        current = self.head
        while current.get_data() != item:
            current = current.get_next()
            pos +=1
        return pos
    
    def insert(self, position, item):
        #adds a new item to the list at the specified position. 
        #This assumes that the item is not already on the list and that the position exists.
        new_node = Node(item)
        previous = None
        current = self.head
        pos = 0
        while pos < position:
            previous = current
            current = current.get_next()
            pos += 1 
        new_node.set_next(current)
        if position == 0:
            self.head = new_node
        else:
            previous.set_next(new_node)
        
    def pop(self, pos = -1):
        #pop() removes the last item from the list and returns it.
        #pop(pos) removes the item at the specified position and returns it.
        previous = None
        current = self.head
        node_count = 0
        """if current.get_next() == None:
            current.set_data("")
            return current """
        while current.get_next() != None:
            if node_count != pos:
                previous = current
                current = current.get_next()
                node_count += 1
            else:
                if previous != None:
                    previous.set_next(current.get_next())
                    pop_result = current
                    current = current.get_next()
                else:
                    self.head = current.get_next()
                    pop_result = current
                    current = current.get_next()
                return pop_result
        pop_result = current
        print(current)
        print(previous)
        previous.set_next(None)
        return pop_result
            
        """if pos == -1:
            while current.get_next() != None: 
                previous = current
                current = current.get_next()
            previous.set_next(None)
        else:
            for i in range(pos):
                previous = current
                current = current.get_next()
            if pos == 0:
                self.head = current.get_next()
            elif pos == -1:
                print(previous.get_next())
                previous.set_next(None)
            else:
                print(current.get_next())
                previous.set_next(current.get_next())"""
                
    def is_empty(self): 
        #returns True if the list is empty.
        return self.length() == 0   
    
    def __repr__(self):
        result = "UnorderedList[" 
        current = self.head
        while current != None:
            result += str(current.get_data()) + ","
            current = current.get_next()
        result += "]"
        return result
    
class ULStack(object):
    def __init__(self):
        self.ul = UnorderedList()
    
    def get_stack(self):
        return self.ul
    
    def size(self):
        return self.ul.length()
    
    def push(self,item):
        #adds item to front of list (aka top of stack)
        self.ul.add(item)
    
    def pop(self):
        #removes item from front of list (aka top of stack)
        if not self.ul.is_empty():
            return self.ul.pop(0).get_data()
    
    def peek(self):
        if not self.ul.is_empty():
            item = self.ul.pop(0).get_data()
            self.ul.add(item)
            return item
    
    def __repr__(self):
        return self.ul.__repr__()
    
class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def hash(self, key):
        return key%self.size
    
    def put(self, key, value):
        hashValue = self.hash(key)
        while self.slots[hashValue] != None:
            hashValue += 1
        self.slots[hashValue] = key
        self.data[hashValue] = value
        
    def get(self, key):
        hashValue = self.hash(key)
        while self.slots[hashValue] != None and self.slots[hashValue] != key:
            hashValue += 1
        return self.data[hashValue]
    
    def __repr__(self):
        """Returns a string representation of the hash table, displayed 
        as two arrays.
        """
        return "Keys:   " + str(self.slots) + "\n" + "Values: " + str(self.data)
    
class BinaryTree(object):
    """
    __init__(key) constructs a binary tree with value key and no children
    get_root_val() returns the root value of this particular sub-tree
    set_root_val(val) modifies the root value of this particular sub-tree
    get_left_child() returns the subtree that is the left child of the current root
    get_right_child() returns the subtree that is the right child of the current root
    insert_left(val) creates a new binary tree and installs it as the left child of the current node, moving the current child down one level in the tree
    insert_right(val) creates a new binary tree and installs it as the right child of the current node, moving the current child down one level in the tree
    """
    def __init__(self, key):
        self.key = key
        self.right_child = None
        self.left_child = None
        
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, val):
        self.key = val
        
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def insert_left(self, val):
        new = BinaryTree(val)
        new.left_child = self.left_child
        self.left_child = new
        
    def insert_right(self, val):
        new = BinaryTree(val)
        new.right_child = self.right_child
        self.right_child = new
                     
    def __repr__(self):
        return "BinaryTree[key=" + str(self.key) + \
            ",left_child=" + str(self.left_child) + \
            ",right_child=" + str(self.right_child) + "]"
    
class BinaryHeap(object):
    """The BinaryHeap class implements the Binary Heap Abstract 
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heap_list = [0]  # not used. Here just to make parent-
                                # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1

    def insert(self,val):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        self.heap_list.append(val)
        self.percolate_up(len(self.heap_list) - 1)
            

    def percolate_up(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        while i//2 > 0 and self.heap_list[i] < self.heap_list[i//2]: # if there is a parent and if current is less than parent value...
            self.heap_list[i//2], self.heap_list[i] = self.heap_list[i], self.heap_list[i//2] # switch values (move up)
            i = i//2 

    def del_min(self):
        """This is a bit trickier. It's easy to return the minimum item,
        the first item on the list, but how do we readjust the heap then?
        """
        top = self.heap_list[1]
        if len(self.heap_list) > 2:
            self.heap_list[1] = self.heap_list.pop()
            self.percolate_down(1)
        else:
            self.heap_list.pop()
        return top

    def percolate_down(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        while i * 2 < len(self.heap_list): # while we have more children...
            min_index = i *2 # assumed, but let's check
            # find the smallest of the children
            if i*2+1 < len(self.heap_list): # if right child exists...
                if self.heap_list[min_index] > self.heap_list[i*2+1]: # compare with left child to find the smallest one
                    min_index = i*2+1
            if self.heap_list[i] > self.heap_list[min_index]: # if the current one is greater than the child
                self.heap_list[i], self.heap_list[min_index] = self.heap_list[min_index], self.heap_list[i] # switch values (move it down)
                i = min_index
            else:
                break
            
    def find_min(self):
        """Returns the minimum item in the heap, without removing it.
        """
        return self.heap_list[1]

    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, vals):
        """Returns a new heap based on a pre-existing list of key 
        values."""
        i = len(vals) // 2
        self.currentSize = len(vals)
        self.heap_list = [0] + vals[:]
        while (i > 0):
            self.percolate_down(i)
            i = i - 1

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)

class Vertex(object):
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is
        connected.
        """
        self.id = key
        self.connected_to = {}   # empty dictionary for neighboring vertices
        self.color = 'white'
        self.distance = 0
        self.predecessor = None
        self.discovery_time = 0     # discovery time
        self.finish_time = 0        # finish time  

    def add_neighbor(self, neighbor_vertex, weight=0):
        """Adds a reference to a neighboring Vertex object to the
        dictionary, to which this vertex is connected by an edge. 
        If a weight is not indicated, default weight is 0.
        """
        self.connected_to[neighbor_vertex] = weight

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_pred(self, predecessor):
        self.predecessor = predecessor

    def get_pred(self):
        return self.predecessor

    def set_discovery(self, discovery_time):
        self.discovery_time = discovery_time

    def get_discovery(self):
        return self.discovery_time

    def set_finish(self, finish_time):
        self.finish_time = finish_time

    def get_finish(self):
        return self.finish_time

    def __repr__(self):
        """Returns a representation of the vertex and its neighbors,
        suitable for printing. Check out the example of 'list
        comprehension' here!
        """
        return 'Vertex[id=' + str(self.id) \
                + ',color=' + self.color \
                + ',dist=' + str(self.distance) \
                + ',pred=' + str(self.predecessor) \
                + ',disc=' + str(self.discovery_time) \
                + ',fin=' + str(self.finish_time) \
            + '] connected_to: ' + str([x.id for x in self.connected_to]) 

    def get_connections(self):
        """Returns the keys of the vertices we're connected to
        """
        return self.connected_to.keys()

    def get_id(self):
        """Returns the id ("key") for this vertex
        """
        return self.id

    def get_weight(self, neighbor_vertex):
        """Returns the weight of an edge connecting this vertex 
        with another.
        """
        return self.connected_to[neighbor_vertex]

class Graph(object):
    """Establishes a graph as a dictionary of vertices, where each entry in
    the dictionary has a key = the id of the vertex, and a value that is the
    Vertex object itself.
    """

    def __init__(self):
        self.graph = {}    # includes keys for vertex objects,
                                # with the value the actual Vertex object

    def add_vertex(self, key):
        """Takes a key value, creates a vertex object for it, and adds that
        object to the vertex dictionary.
        """
        new_vertex = Vertex(key)
        self.graph[key] = new_vertex   # maps key to Vertex
        return new_vertex

    def get_vertex(self, key):
        """Returns the Vertex object associated with this key"""
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None

    def __contains__(self, vertex):
        """Allows us to use the "in" operator"""
        return vertex in self.graph.keys()

    def add_edge(self, fromKey, toKey, weight=0):
        """If we don't already have a Vertex object for either key, create
        one and add it to the vertex dictionary. Then add the second vertex
        as a neighbor to the first, thus creating an edge in the graph.
        """
        if fromKey not in self.graph.keys():
            self.add_vertex(fromKey)
        if toKey not in self.graph.keys():
            self.add_vertex(toKey)
        self.graph[fromKey].add_neighbor(self.graph[toKey], weight)

    def get_vertices(self):
        return self.graph.keys()

    def __iter__(self):
        """Allows us to iterate through the vertices in the graph:
        for vertex in graph:
            # do something with vertex
        """
        return iter(self.graph.values())

# for testing purposes...
def main():
    v = Vertex("Ava")
    #print(v.set_color("white"))
    print(v.get_color())
    
    
    
    
if __name__ == "__main__":
    main()
