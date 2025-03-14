class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# Create nodes
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')

# Connect nodes
A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

# DFS Traversal Function
def dfs(node):
	if node is not None:
		print(node.value)  # Process the node (e.g., print it)
		dfs(node.left)     # Traverse left subtree
		dfs(node.right)    # Traverse right subtree

# Perform DFS traversal
print("DFS Traversal of the tree:")
dfs(A)
