# This class creates the nodes 
class Node:
    def __init__(self, data):
        # data that will be stored 
        self.data = data
        # reference to identify where the data is in the linked list
        self.ref = None
# This class creates the linked list
class Linked_list:
    def __init__(self):
        # This head instance is the starting point of the list
        self.head = None

    def check_list(self):
        if (self.head == None):
            print('The list is empty!!')
        else:
            x = self.head
            while x != None:
                print(x.data)
                x = x.ref
    
    # add data to list by creating a node
    def add(self, data):
        # creates new node
        new_node = Node(data)
        # assigning the nodes reference to the starting point which is head
        new_node.ref = self.head
        # now we are saying assign the new node to head
        self.head = new_node

    # adds data to the end of the list
    def add_to_end(self, data):
        # creates new node
        new_node = Node(data)
        # determines if the head is empty
        if(self.head == None):
            # if the head is empty then place the new node in the first position of the list
            self.head = new_node
        else:
            # else loop through the list and check if the reference is empty
            x = self.head
            while x.ref != None:
                x = x.ref
            # if it is empty then place the new node in the last position in the list
            x.ref = new_node
    # removes the first item in the list
    def remove_item(self):
        if(self.head == None):
            print('You can not remove item due to list being empty')
        else:
            self.head = self.head.ref
                




first_list = Linked_list()
first_list.add_to_end('C#')
first_list.add_to_end('C++')
first_list.add_to_end('Java')
first_list.add('Python')
first_list.add('PHP')
first_list.remove_item()
first_list.check_list()

