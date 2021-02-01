class Node:
    def __init__(self, data):
        self.data = data
        

class List_binary:
    def __init__(self):
        self.root_node = None
        self.left_child = None
        self.right_child = None

    def append_binary_tree(self, data):
        # creates new node
        new_node = Node(data)
        # checking if root node is empty
        if (self.root_node == None):
            # traverse through the array to assign the first value as the root-node
            # assigning the new node as the root node
            self.root_node = new_node
            print(self.root_node.data)            
        else:
            # keep track of where you are in the tree by traversing and assigning parent_node
            # as the current root of its respective child
            current_node = self.root_node
            parent_node = None
            while parent_node:
                parent_node = current_node
    
            # check is the root node is a greater than
            # place child on the left side of the tree
            # append to the tree
            if (current_node.data > new_node.data):
                current_node = self.left_child
                if (current_node == None or new_node.data < current_node.data or new_node.data > current_node.data):
                    if (current_node != None):
                        if (new_node.data > current_node.data):
                            self.right_child = new_node
                            parent_node = self.right_child
                            print(parent_node.data)
                            return
                        parent_node = current_node
                        current_node = new_node
                        print(current_node.data)
                    else:
                        self.left_child = new_node
                        parent_node = self.left_child
                        print(parent_node.data)
                    return
               
            else:
               # if its greater than place child on the right side of the tree
                current_node = self.right_child
                if(current_node == None or new_node.data > current_node.data):
                    self.right_child = new_node
                    parent_node = self.right_child
                    print(parent_node.data)
                    return
                

newBST = List_binary()