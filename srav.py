import matplotlib.pyplot as plt

p = 0.33
a = 4.0
b = 7.0

with open("data-" + str(p) + '-' + str(a) + '-' + str(b), 'r') as f:
	vals = [float(line) for line in f if float(line) <= 1.0]

plt.scatter(vals, vals)
plt.show()
