
from graphviz import Digraph
import time 

#fixme for the split screen: make 3 subgraphs
# node class
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'
    
# RBT class
class RedBlackTree:
    #initializer
    def __init__(self):
        self.root = None
    
    #left rotation function
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

    #right rotation function
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

    # insert node into tree as if BST
    def treeInsert(self, node):
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

    # insert node and balance tree after
    def insertNode(self,val):
        x = Node(val)
        self.treeInsert(x)
        x.color = 'red'

        # Fails to check for existence of x.parent ? 

        while x.parent and x.parent.color == 'red': #fixme infinite loop when 10 used
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y and y.color == 'red':
                    x.parent.color = 'black'
                    y.color = 'black'
                    x.parent.parent.color = 'red'
                    x = x.parent.parent
                #elif x == x.parent.right:
                else:
                    if (x == x.parent.right):
                        x = x.parent
                        self.rotateLeft(x)                        
                    x.parent.color = 'black'
                    x.parent.parent.color = 'red'
                    self.rotateRight(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y and y.color == 'red': #fixme maybe breaking here
                    x.parent.color = 'black'
                    y.color = 'black'
                    x.parent.parent.color = 'red'
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.rotateRight(x)
                    x.parent.color = 'black'
                    x.parent.parent.color = 'red'
                    self.rotateLeft(x.parent.parent)
        self.root.color = 'black'

    #function to generate directed graph of tree
    def reload(self):   
        cur = self.root
        treeGraph = Digraph()
        if cur is not None:
            treeGraph.node(name = str(cur), label = str(cur.value), style = "filled", fontcolor = "white", color = str(cur.color), shape = "circle")                     
        return self.build_tree(cur, treeGraph)

    # add each node and arrow to graph
    def build_tree(self, cur, treeGraph):              
        if cur.left is not None:         
            treeGraph.node(name = str(cur.left), label = str(cur.left.value), style = "filled", fontcolor = "white", color = str(cur.left.color), shape="circle")
            treeGraph.edge(str(cur), str(cur.left))
            treeGraph = self.build_tree(cur.left, treeGraph = treeGraph)               
        if cur.right is not None: 
            treeGraph.node(name = str(cur.right), label = str(cur.right.value), style = "filled", fontcolor = "white", color = str(cur.right.color), shape="circle")
            treeGraph.edge(str(cur), str(cur.right))
            treeGraph = self.build_tree(cur.right, treeGraph = treeGraph)
        return treeGraph


Tree1 = RedBlackTree()
Tree1.insertNode(14)
Tree1.insertNode(15)
Tree1.insertNode(11)
Tree1.insertNode(13)
Tree1.insertNode(12)
Tree1.insertNode(10)
Tree1.insertNode(19)
Tree1.insertNode(17)
Tree1.insertNode(10)
Tree1.insertNode(16)

for i in range(10):
    Tree1.insertNode(int(i))
    
    RBTshow = Tree1.reload()
    RBTshow.render("Red-Black Tree", view = True)
    time.sleep(1)

