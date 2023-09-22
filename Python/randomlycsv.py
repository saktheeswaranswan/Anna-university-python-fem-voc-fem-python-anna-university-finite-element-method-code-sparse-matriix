import random

def swap_number_position(line):
    numbers = line.strip().split(',')
    if len(numbers) >= 2:
        second_number = numbers[1]
        new_position = random.randint(1, 4)  # Change to 4 since the list is 0-indexed
        numbers[1] = numbers[new_position]
        numbers[new_position] = second_number
    return ','.join(numbers)

# Read input from the text file
input_file_path = 'NCA.txt'
output_file_path = 'output.txt'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

output_lines = [swap_number_position(line) for line in lines]

# Write output to the text file
with open(output_file_path, 'w') as file:
    file.write('\n'.join(output_lines))

# Print output
for line in output_lines:
    print(line)

