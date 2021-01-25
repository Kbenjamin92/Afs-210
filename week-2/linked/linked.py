# This class creates the nodes 
class Node:
    def __init__(self, data):
        # data that will be stored 
        self.data = data
        # reference to identify where the data is in the linked list
        self.next = None
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
                x = x.next



first_list = Linked_list()
first_list.check_list()

