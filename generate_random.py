from random import random
import sys
# print(dat)
# exit()
# p = 0.4 # [0;1]
# a = 0.8   # [0;10]
# b = 8  # [0;10]

def generateNumber(p, a, b):
	num = random() # [0;1]
	if num < p:
		num = random() * a # [0;a]
		if num > p:
			num = random() * b # [0;b]
	return num

def parseData(p, a, b):
	numbers = [generateNumber(p, a, b) for i in range(1000)]
	with open("srav2", 'w') as f:
		for i in range(1000):
			if numbers[i] <= 1.0:
				f.write(str(numbers[i]) + ', ')

if __name__ == '__main__':
	p, a, b = list(map(float, [sys.argv[i] for i in range(1, 4)]))
	# print(p, a, b)
	parseData(p, a, b)
