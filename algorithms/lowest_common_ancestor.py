# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 
def findNode(root,k):
# Find a node k in a binary tree given a root of the tree
    if root == None:
        return False
    if root.key == k:
        return True
    else:
        return findNode(root.left,k) or findNode(root.right,k)

# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path 
# exists otherwise false
def findPath(root, k, path):

    if root == None:
        return path

    path.append(root.key)

    if k in path:
        return path

    if root == k:
        return path
    else:
        if findNode(root.left,k):
            path = findPath(root.left,k,path)
        if findNode(root.right,k):
            path = findPath(root.right,k,path)  
        return path

# Returns LCA if node n1 , n2 are present in the given
# binary tree otherwise return -1
def findLCA(root, n1, n2):

    lca = 0

    path1 = []
    path2 = []

    path1 = findPath(root,n1,path1)
    path2 = findPath(root,n2,path2)

    path1.remove(n1)
    path2.remove(n2)

    print(path1)
    print(path2)

    if n1 in path2:
        lca = n1
    elif n2 in path1:
        lca = n2
    else:
        for node1 in path1:
            for node2 in path2:
                if node1 == node2:
                    lca = node1
        
    return lca
    
   
 
# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
##print("LCA(4, 5) = %d" %(findLCA(root, 4, 5)))
##print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
##print("LCA(3, 4) = %d" %(findLCA(root,3,4)))
print("LCA(2, 4) = %d" %(findLCA(root, 2, 4)))

## solutions
## LCA(4, 5) = 2
## LCA(4, 6) = 1
## LCA(3, 4) = 1
## LCA(2, 4) = 2

print(findPath(root,6,[]))