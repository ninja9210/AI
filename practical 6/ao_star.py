class Node:
	def __init__(self, name, cost=0):
		self.name = name
		self.cost = cost
		self.children = []
		self.parent = None 

	def __repr__(self):
		return f"Node({self.name}, {self.cost})"

def reconstruct_path(node):
	path = []
	while node:
		path.append(node.name)
		node = node.parent
	return path[::-1]  

def ao_star(start_node, goal_node):
	open_set = [start_node]
	closed_set = set()
	while open_set:
		current_node = min(open_set, key=lambda node: node.cost)  
		if current_node == goal_node:
			return reconstruct_path(current_node)  
		open_set.remove(current_node)
		closed_set.add(current_node)
		for child in current_node.children:
			if child not in closed_set:
				child.cost = current_node.cost + child.cost
				child.parent = current_nod
				if child not in open_set:
					open_set.append(child)
	return None  


start = Node('Start', 0)
goal = Node('Goal', 0)

node_a = Node('A', 1)
node_b = Node('B', 2)
start.children = [node_a, node_b]

node_a1 = Node('A1', 1)
node_a2 = Node('A2', 1)
node_a.children = [node_a1, node_a2]

node_b1 = Node('B1', 1)
node_b2 = Node('B2', 2)
node_b.children = [node_b1, node_b2]

node_b2.children = [goal]

path = ao_star(start, goal)
print("Path found:", path)
