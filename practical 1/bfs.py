class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')


A.left = B
A.right = C
B.left = D
B.right = E
C.right = F


from collections import deque
def bfs(root):
	if root is None:
		return
	queue = deque([root]) 
	while queue:
		node = queue.popleft() 
		print(node.value) 
		if node.left:
			queue.append(node.left)
		
		if node.right:
			queue.append(node.right)


print("BFS Traversal of the tree:")
bfs(A)
