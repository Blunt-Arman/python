import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,50,44,55,60,30,40,40,20,40,120])
y = np.array([100,240,350,450,500,400,200,400,500,230,650])

plt.plot(x,y)
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burnage")
plt.grid()
plt.show()
