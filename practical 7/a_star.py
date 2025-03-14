import heapq
def a_star_search(graph, start, goal, heuristic):
	open_list = []
	heapq.heappush(open_list, (0 + heuristic[start], start)) # (f, node)
	g_costs = {start: 0}
	parent = {start: None}
	while open_list:
		_, current = heapq.heappop(open_list)
		if current == goal:
			# Reconstruct the path
			path = []
			while current:
				path.append(current)
				current = parent[current]
			return path[::-1]
		for neighbor, cost in graph[current].items():
			g_cost = g_costs[current] + cost
			if neighbor not in g_costs or g_cost < g_costs[neighbor]:
				g_costs[neighbor] = g_cost
				f_cost = g_cost + heuristic[neighbor]
				heapq.heappush(open_list, (f_cost, neighbor))
				parent[neighbor] = current
	return None # No path found
# Example graph with edge costs
graph = {
 'A': {'B': 1, 'C': 3},
 'B': {'A': 1, 'D': 2, 'E': 5},
 'C': {'A': 3, 'E': 1},
 'D': {'B': 2},
 'E': {'B': 5, 'C': 1}
}
# Heuristic values for each node (estimated cost to goal)
heuristic = {
 'A': 4,
 'B': 2,
 'C': 3,
 'D': 1,
 'E': 0
}
# Running A* search
start_node = 'A'
goal_node = 'E'
path = a_star_search(graph, start_node, 
goal_node, heuristic)
if path:
 print("Path found:", path)
else:
 print("No path found")
