class Node:
    def __init__(self, data):
        self.data = data
        self.left_side = None
        self.right_side = None
        self.left_container = []
        self.right_container = []

# Sorting the list seperating the child nodes
    def add(self, data):
        if (self.data):
            for i in data:
                if (self.data == i):
                    root = i
                    print(root)
                if (i < self.data):
                    if (self.left_side == None or self.left_side.data < i):
                        self.left_side = Node(i)
                        self.left_container.append(self.left_side.data)
                    else:
                        self.left_side.add(i)

                elif (i > self.data):
                    if (self.right_side == None or self.right_side.data < i):
                        self.right_side = Node(i)
                        self.right_container.append(self.right_side.data)
                    else:
                        self.right_side.add(i)
        else:
            self.data = data

# order the left child node
    def display_left_tree(self):
        parent_node = 2
        for i in self.left_container:
            if (i == parent_node):
                print(i)
            else:
                pass
           
        for left_item in self.left_container:
                if (left_item < parent_node):
                    print(left_item)
                elif (left_item > parent_node):
                    print(left_item)

# order the right child node
    def display_right_tree(self):
        parent_node = 6
        for i in self.right_container:
            if (i == parent_node):
                print(i)
            else:
                pass
           
        for right_item in self.right_container:
                if (right_item < parent_node):
                    print(right_item)
                elif (right_item > parent_node):
                    print(right_item)
        
        print(None)
            
        

root = Node(4)
root.add([1,2,3,4,5,6,7])
root.display_left_tree()
root.display_right_tree()


