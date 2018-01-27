import matplotlib.pyplot as plt
import numpy as np

p = 0.33
a = 4.0
b = 7.0

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
y, x, _ = plt.hist(vals, bins=100)
print("Y = ", y)
print("X = ", x)
print("_ = ", _)
plt.show()

def calc(i):
	ret = 0.0
	for v in vals:
		if v >= i and v < i + 0.01:
			ret += 1
	return float(ret / len(vals))

diff = 0
per = 0
prev = calc(0.0)
for i in np.arange(0.01, 1.0, 0.01):
	now = calc(i)
	if now - prev > diff and (calc(i + 0.01) - now > now - prev or prev - calc(i - 0.02) > now - prev):
		diff = now
		per = i
	prev = now

print("DIff = ", per)
