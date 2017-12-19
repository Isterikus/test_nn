from random import random
import matplotlib.pyplot as plt
import numpy as np
# dat = np.random.random(200).reshape(20,10) # создаём матрицу значений
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
	with open("data", 'w') as f:
		for i in range(1000):
			f.write(str(numbers[i]) + '\n')

def findVars():
	with open("data", 'r') as f:
		vals = [float(line) for line in f]
	# print(vals)
	classificate_below_1 = [0 for i in range(10)]
	classificate_grather_1 = [0 for i in range(10)]
	for val in vals:
		if val < 1:
			classificate_below_1[int(val * 10)] += 1
		else:
			classificate_grather_1[int(val)] += 1
	# print("All: ", len(vals))
	# print("Less than one: ", less_one)
	mx = max(vals)
	less = sum(classificate_below_1) - (1 / mx) * len(vals)
	# print("LESS = ", less)
	return {'less': less, 'razbr': classificate_below_1}
	# print("LESS 1: ", sum(classificate_below_1))
	# for i in range(10):
		# print("0.", i, " = ", classificate_below_1[i])
	# print("GRATHER 1: ", sum(classificate_grather_1))
	# for i in range(10):
		# if i != 0:
			# print(i, " = ", classificate_grather_1[i])

def test():
	p_tests = [i/10 for i in range(1, 10)]
	a_tests = [i for i in range(1, 10)]
	b_tests = [5]

	data = [[],[],[],[]]
	# p_tests = [0.1]
	k = 0
	i = 0
	razbr = []
	for b in b_tests:
		i = 0
		# for p in p_tests:
		for a in a_tests:
			data[k].append([])
			razbr.append([])
			# for a in a_tests:
			for p in p_tests:
				# print("P = ", p, " | A = ", a)
				parseData(p, a, b)
				vals = findVars()
				data[k][i].append(vals['less'])
				razbr[i].append(vals['razbr'])
			i += 1
			# razbr[i] = [vl for vl in razbr[i]]
		k += 1
	for r in range(len(razbr)):
		sm = [0 for i in range(len(razbr[r][k]))]
		for k in range(len(razbr[r])):
			for srab in range(len(razbr[r][k])):
				sm[srab] += razbr[r][k][srab]
		razbr[r] = [vl/len(sm) for vl in sm]
	i = 0
	for i in range(len(razbr)):
		al = sum(razbr[i])
		razbr[i] = [float("{0:.2f}".format((vl/al)*100)) for vl in razbr[i]]
		print(razbr[i])
		print(sum(np.diff(razbr[i])))
		print(max(razbr[i]) - min(razbr[i]))
		i += 1
	# print(razbr)
	# for i in range(1):
	# fig = plt.figure()
	# pc = plt.pcolor(data[i]) # метод псевдографики pcolor
	# plt.colorbar(pc)
	# plt.xlabel("A")
	# plt.ylabel("P")
	# plt.title('Simple pcolor plot')
	# plt.show()

	fig = plt.figure()
	pc = plt.pcolor(razbr) # метод псевдографики pcolor
	plt.colorbar(pc)
	plt.xlabel("A")
	plt.ylabel("P")
	plt.title('Simple pcolor plot')
	plt.show()

if __name__ == '__main__':
	# parseData()
	# findVars()
	print("----------------------------------------------------------------------------------")
	test()