
import matplotlib.pyplot as plt
from read_data import *

x = data[:,0]
y = data[:,1]
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x, y)
plt.title("Web Traffic over the Last Month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")

plt.xticks([w * 7 * 24 for w in range(10)], ["week %i" % w for w in range(10)])
plt.autoscale(tight = True)
plt.grid()
plt.show()