import re
total = 0
f = open('input', 'r', encoding='utf-8')
for line in f:
	line = line.replace("one", "o1ne").replace("two", "t2wo").replace("three", "t3hree").replace("four", "f4our").replace("five", "f5ive").replace("six", "s6ix").replace("seven", "s7even").replace("eight", "e8ight").replace("nine", "n9ine")
	matches = re.findall(r'\d', line)
	total = total + int(str(matches[0]) + str(matches[len(matches)-1]))

f.close()

print(total)
