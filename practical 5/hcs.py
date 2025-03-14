def simple_hill_climbing(numbers):
	current_index = 0 
	while True:
		if current_index + 1 < len(numbers):
			if numbers[current_index] < numbers[current_index + 1]:
				current_index += 1 
			else:
				return numbers[current_index]
		else:
			return numbers[current_index]

numbers = [1, 3, 7, 12, 9, 5]
max_number = simple_hill_climbing(numbers)
print(f"The maximum number in the list is: {max_number}")