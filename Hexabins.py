import matplotlib.pyplot as plt
import numpy as np

#Generate some sample data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

#Create the Hexabin plot
plt.hexbin(x, y, gridsize=50, cmap='Greens')
plt.colorbar()

#Show the plot
plt.show()