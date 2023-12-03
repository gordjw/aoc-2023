import re

def string_to_number(number_word):
	match number_word:
		case "zero":
			return 0
		case "one":
			return 1
		case "ne":
			return 1
		case "two":
			return 2
		case "wo":
			return 2
		case "three":
			return 3
		case "hree":
			return 3
		case "four":
			return 4
		case "our":
			return 4
		case "five":
			return 5
		case "ive":
			return 5
		case "six":
			return 6
		case "ix":
			return 6
		case "seven":
			return 7
		case "even":
			return 7
		case "eight":
			return 8
		case "ight":
			return 8
		case "nine":
			return 9
		case "ine":
			return 9
		case _:
			return int(number_word)

total = 0

f = open('input', 'r', encoding='utf-8')

for line in f:
	print("=======================")
	# Extract all the numbers from each line
	matches = re.findall(r'((?<=o)ne|(?<=t)wo|(?<=t)hree|(?<=f)our|(?<=f)ive|(?<=s)ix|(?<=s)even|(?<=e)ight|(?<=n)ine|one|two|three|four|five|six|seven|eight|nine|\d)', line)
	print(line)
	print(matches)

	# Add the numbers to the total:
	#   - Create a two digit number, using the first number on the line and the last number on the line
	#   - First and last might be the same digit
	#   - Add that number to the total
	first_digit = string_to_number(matches[0])
	second_digit = string_to_number(matches[len(matches)-1])
	final_number = int(str(first_digit) + str(second_digit))

	print(first_digit, second_digit, final_number)

	total = total + final_number

f.close()

print(total)