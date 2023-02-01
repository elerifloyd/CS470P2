from graphviz import Digraph

#fixme for the split screen: make 3 subgraphs
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'blue'
    
   
class SplayTree:

    def __init__(self):
        self.root = None
    
    def rotateLeft(self, node):
        y = node.right
        node.right = y.left

        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        
        y.left = node
        node.parent = y

    def rotateRight(self, node):
        y = node.left
        node.left = y.right

        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        
        y.right = node
        node.parent = y

    def treeInsert(self, x):
        node = Node(x)
        print(f'Inserting node {node.value}')
        
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        self.splay(node)

    def splay(self, x): 
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.left:
                    # zig rotation
                    self.rotateRight(x.parent)
                else:
                    # zag rotation
                    self.rotateLeft(x.parent)
            elif (x == x.parent.left) and (x.parent == x.parent.parent.left):
                # zig-zig rotation
                self.rotateRight(x.parent.parent)
                self.rotateRight(x.parent)
            elif (x == x.parent.right) and (x.parent == x.parent.parent.right):
                # zag-zag rotation
                self.rotateLeft(x.parent.parent)
                self.rotateLeft(x.parent)
            elif (x == x.parent.right) and (x.parent == x.parent.parent.left):
                    # zig-zag rotation
                    self.rotateLeft(x.parent)
                    self.rotateRight(x.parent)
            else:
                    # zag-zig rotation
                    self.rotateRight(x.parent)
                    self.rotateLeft(x.parent)

    def search(self, value):
        node = self.treeSearch(self.root, value)
        if node is not None:
            self.splay(node)

    def treeSearch(self, cur, value):
        if cur is None or value == cur.value:
            return cur
        if value < cur.key:
            self.treeSearch(cur.left, value)
        else:
            self.treeSearch(cur.right, value)

    # function to generate directed graph of tree
    def reload(self):   
        cur = self.root
        treeGraph = Digraph()
        if cur is not None:
            treeGraph.node(name = str(cur), label = str(cur.value), fontcolor = "black", color = str(cur.color), shape = "circle")                     
        return self.build_tree(cur, treeGraph)

    # add each node and arrow to graph
    def build_tree(self, cur, treeGraph):              
        if cur.left is not None:         
            treeGraph.node(name = str(cur.left), label = str(cur.left.value), fontcolor = "black", color = str(cur.left.color), shape="circle")
            treeGraph.edge(str(cur), str(cur.left))
            treeGraph = self.build_tree(cur.left, treeGraph = treeGraph)               
        if cur.right is not None: 
            treeGraph.node(name = str(cur.right), label = str(cur.right.value), fontcolor = "black", color = str(cur.right.color), shape="circle")
            treeGraph.edge(str(cur), str(cur.right))
            treeGraph = self.build_tree(cur.right, treeGraph = treeGraph)
        return treeGraph


Tree1 = SplayTree()
Tree1.treeInsert(4)
Tree1.treeInsert(5)
Tree1.treeInsert(1)
Tree1.treeInsert(3)
Tree1.treeInsert(2)
Tree1.treeInsert(0)
Tree1.treeInsert(9)
Tree1.treeInsert(7)
Tree1.treeInsert(10)
Tree1.treeInsert(100)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", view = True)