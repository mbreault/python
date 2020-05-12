#!/usr/bin/env python3

import sys

class Node():
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        print(self.data)

def insert(node,data):
    if (node == None):
        node = Node(data)
    else:
        if (data <= node.data): 
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)

    return(node)

def lookup(node, target): 
        if node == None:
            return(False)
        else:
            if (target == node.data): return(True)
            else:
                if (target < node.data): return(lookup(node.left, target))
                else: return(lookup(node.right, target))    

def size(node):
    if node == None:
        return 0
    else:
        return 1 + size(node.left) + size(node.right)

def printTree(node):
    if node == None: return ""
    
    printTree(node.left)
    print(node.data, end="")
    printTree(node.right)
        
def maxDepth(node):
    if node == None:
        return 0
    else:
        left_depth = maxDepth(node.left)
        right_depth = maxDepth(node.right)
        if (left_depth > right_depth):
            return left_depth+1
        else:
            return right_depth+1

def minValue(node):
    current = node
    while (current.left != None):
        current = current.left

    return(current.data)

def getNodeValue(node):
    if node != None:
        return node.data
    else:
        return None

def printNodes(node):
    if node == None: return None
    else:
        printNodes(node.left)
        printNodes(node.left)
        print(node.data,node.left,node.right)
        

def printPostOrder(node):
    if node == None: return ""
    
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data, end="")

def build123():
    root = insert(None,2)
    root = insert(root,1)
    root = insert(root,3)
    return root

def build12345():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 

    return root

root = build12345()
printTree(root)
print()
printPostOrder(root)
print()
print("Size",size(root))
print("Depth",maxDepth(root))
print("MinValue",minValue(root))
print(root.data,root.left.data,root.right.data)
left = root.left
print(left.data,left.left.data,left.right.data)



