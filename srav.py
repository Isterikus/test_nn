import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

p = 0.5
a = 3.0
b = 8.0

with open("data-" + str(p) + '-' + str(a) + '-' + str(b), 'r') as f:
	vals = np.array([float(line) for line in f if float(line) <= 1.0])

# df =
# plt.scatter(vals, vals)
df = pd.DataFrame(vals)
# plt.show()
print(df.quantile([.1, .5]))


