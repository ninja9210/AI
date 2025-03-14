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

# BFS Traversal Function
from collections import deque
def bfs(root):
	if root is None:
		return
	queue = deque([root]) # Initialize the queue with the root node 
	while queue:
		node = queue.popleft() # Dequeue the front node
		print(node.value) # Process the node (e.g., print it)
		# Enqueue left child if it exists
		if node.left:
			queue.append(node.left)
		# Enqueue right child if it exists
		if node.right:
			queue.append(node.right)

# Perform BFS traversal
print("BFS Traversal of the tree:")
bfs(A)