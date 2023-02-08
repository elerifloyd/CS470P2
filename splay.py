from graphviz import Digraph
import time

#fixme for the split screen: make 3 subgraphs
class Node:
    #node initializer
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'blue'
    
class SplayTree:

    #tree initializer
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

    #create and insert node given a value
    #performs BST insert then calls splay on the new node
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

    #splay function, uses rotations to move node x to root
    def splay(self, x): 
        while x.parent is not None:
            if x.parent == self.root:
                if x == x.parent.left:
                    self.rotateRight(x.parent)
                else:
                    self.rotateLeft(x.parent)
            elif (x == x.parent.left) and (x.parent == x.parent.parent.left):
                self.rotateRight(x.parent.parent)
                self.rotateRight(x.parent)
            elif (x == x.parent.right) and (x.parent == x.parent.parent.right):
                self.rotateLeft(x.parent.parent)
                self.rotateLeft(x.parent)
            elif (x == x.parent.right) and (x.parent == x.parent.parent.left):
                self.rotateLeft(x.parent)
                self.rotateRight(x.parent)
            else:
                self.rotateRight(x.parent)
                self.rotateLeft(x.parent)

    #finds node using BST search
    def treeSearch(self, cur, value):
        if cur is None or value == cur.value:
            return cur
        if value < cur.value:
            return self.treeSearch(cur.left, value)
        else:
            return self.treeSearch(cur.right, value)

    #call BST search, then call splay on node if found
    def search(self, value):
        node = self.treeSearch(self.root, value)
        #node.color = 'green'
        if node is not None:
            self.splay(node)
        return node

    #find maximum node value in tree by traversing to the farthest right node
    def treeMax(self, cur):
        while cur.right != None:
            cur = cur.right
        return cur

    #function to delete node
    def delete(self, value):
        print(f'Deleting node {value}')
        node = self.search(value)
        if node is not None:
            self.splay(node)

            left = SplayTree()
            left.root = self.root.left
            if left.root != None:
                left.root.parent = None

            right = SplayTree()
            right.root = self.root.right
            if right.root != None:
                right.root.parent = None

            if left.root is not None:
                max = self.treeMax(left.root)
                left.splay(max)
                left.root.right = right.root
                self.root = left.root
            else:
                self.root = right.root
        else:
            print("Node not found")

    # function to generate directed graph of tree
    def reload(self):   
        cur = self.root
        graph_attrs = {
            'label' : 'Splay Tree',
            'labelloc' : 't'}
        treeGraph = Digraph(graph_attr = graph_attrs)
        if cur is not None:
            treeGraph.node(name = str(cur), label = str(cur.value), fontcolor = "black", color = str(cur.color), shape = "circle")                     
        return self.build_tree(cur, treeGraph)

    # add each node and arrow to graph
    def build_tree(self, cur, treeGraph):              
        if cur.left is not None:         
            treeGraph.node(name = str(cur.left), label = str(cur.left.value), fontcolor = "black", color = str(cur.left.color), shape = "circle", fixedsize = 'true')
            treeGraph.edge(str(cur), str(cur.left))
            treeGraph = self.build_tree(cur.left, treeGraph = treeGraph)               
        if cur.right is not None: 
            treeGraph.node(name = str(cur.right), label = str(cur.right.value), fontcolor = "black", color = str(cur.right.color), shape = "circle", fixedsize = 'true')
            treeGraph.edge(str(cur), str(cur.right))
            treeGraph = self.build_tree(cur.right, treeGraph = treeGraph)
        return treeGraph

Tree1 = SplayTree()
Tree1.treeInsert(4)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(5)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(1)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(3)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(2)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(0)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.treeInsert(100)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.delete(4)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(3)
Tree1.delete(3)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)
time.sleep(5)
Tree1.search(2)
SplayShow = Tree1.reload()
SplayShow.render("Splay Tree", format = 'pdf', view = True)