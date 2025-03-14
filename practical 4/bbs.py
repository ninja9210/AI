def branch_bound(nums, limit):
	n = len(nums)
	max_sum = 0
	best_chosen_numbers = []
	queue = [(0, 0, [])]
	
	while queue:
		index, current_sum, chosen_numbers = queue.pop(0)
		
		if index == n:
			if current_sum <= limit:
				if current_sum > max_sum:
					max_sum = current_sum
					best_chosen_numbers = chosen_numbers  # Update the best chosen numbers
			continue
		
		if current_sum + nums[index] <= limit:
			queue.append((index + 1, current_sum + nums[index], chosen_numbers + [nums[index]]))
		
		queue.append((index + 1, current_sum, chosen_numbers))
	
	# Print the best chosen numbers
	print(f"Best chosen numbers: {best_chosen_numbers}")
	return max_sum

if __name__ == "__main__":
	numbers = [10, 20, 30, 40]
	limit = 50
	result = branch_bound(numbers, limit)
	print(f"Maximum sum under limit {limit}: {result}")