import re

total = 0

f = open('input', 'r', encoding='utf-8')

for line in f:
	# Extract all the numbers from each line
	matches = re.findall(r'\d',line)

	# Add the numbers to the total:
	#   - Create a two digit number, using the first number on the line and the last number on the line
	#   - First and last might be the same digit
	#   - Add that number to the total
	total = total + int(matches[0]+matches[len(matches)-1])

f.close()

print(total)
