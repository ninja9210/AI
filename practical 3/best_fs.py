from queue import PriorityQueue

def greedy_best_first_search(start, goal, heuristic, graph):
	open_list = PriorityQueue()
	open_list.put((heuristic[start], start)) 
	visited = set()
	came_from = {} # Tracks the path

	while not open_list.empty():
		cost, current = open_list.get()

		if current == goal:
		
			path = []
			while current is not None:
				path.append(current)
				current = came_from.get(current, None)
			return path[::-1] 

		visited.add(current)

		for neighbor, _ in graph.get(current, []):
			if neighbor not in visited:
				came_from[neighbor] = current
				open_list.put((heuristic[neighbor], neighbor))

	return None


graph = {
	'A': [('B', 2), ('C', 1)],
	'B': [('A', 2), ('D', 3)],
	'C': [('A', 1), ('E', 4)],
	'D': [('B', 3), ('G', 5)],
	'E': [('C', 4), ('F', 2)],
	'F': [('E', 2), ('G', 1)],
	'G': [('D', 5), ('F', 1)],
}

heuristic = {
	'A': 5,
	'B': 4,
	'C': 7,
	'D': 3,
	'E': 6,
	'F': 2,
	'G': 0,
}

start_state, goal_state = 'A', 'G'
print("Path found:", greedy_best_first_search(start_state, goal_state, heuristic, graph))
