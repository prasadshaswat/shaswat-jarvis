class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')
        
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("Inorder traversal of the BST:")
inorder(r)
print("\nPreorder traversal of the BST:")
preorder(r)
print("\nPostorder traversal of the BST:")
postorder(r)

def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        
        return max(lDepth, rDepth) + 1

print("\nHeight of the tree is %d" % (maxDepth(r)))

# Correcting findLevel and adding logic for "height" (considering it as level for understanding)
def findLevel(root, key, level):
    if root is None:
        return -1
    if root.val == key:
        return level
    left = findLevel(root.left, key, level + 1)
    if left != -1:
        return left
    return findLevel(root.right, key, level + 1)

level = findLevel(r, 60, 0)
print("Level of the node with value 60 is %d" % level)

