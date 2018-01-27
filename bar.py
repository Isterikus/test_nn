import matplotlib.pyplot as plt
import numpy as np

p = 0.8
a = 3.0
b = 8.0

with open("data-" + str(p) + '-' + str(a) + '-' + str(b), 'r') as f:
	vals = [float(line) for line in f if float(line) <= 1.0]


gr = 0
less = 0
for i in vals:
	if i <= 0.8:
		less += 1
	elif i <= 1.0:
		gr += 1

print("LESS = ", less)
print("GR   = ", gr)
# plt.bar(x, y)
# plt.show()
# plt.hist(vals, bins=100)
# plt.show()
