import matplotlib.pyplot as plt
import numpy as np

p = 0.33
a = 4.0
b = 7.0

with open("data-" + str(p) + '-' + str(a) + '-' + str(b), 'r') as f:
	vals = [float(line) for line in f]

arr = []
spl = 20
for i in range(spl):
	arr.append([])
	st = i/spl
	end = round(st + 1/spl, 2)
	for v in vals:
		if v >= st and v < end:
			arr[i].append(v)
	# print("[" + str(st) + ", " + str(end) + "] = ", len(arr[i]))

# plt.bar(np.arange(0, 10, 0.5), [len(arr[i]) for i in range(spl)])
# plt.bar()
# plt.show()

def calc_diff(compare):
	less = 0
	gr = 0
	for i in vals:
		if i <= compare:
			less += 1
		elif i <= 1.0:
			gr += 1
	return (less, gr)

# less, gr = calc_diff(1.0)
# print("Less = ", less)
# print ("GR =  ", gr)

best = 1000
best_diff = 1000
for i in np.arange(0.0, 1.0, 0.0001):
	less, gr = calc_diff(i)
	perc = abs(less - gr)
	if perc < best_diff:
		# print(less, gr)
		best = i
		best_diff = perc

print("P = ", best)
