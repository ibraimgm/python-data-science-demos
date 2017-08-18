import numpy as np
import matplotlib.pyplot as plt

iris_data = np.genfromtxt('data/iris.data',delimiter=',')
setosa = iris_data[:50,2]
versicolor = iris_data[50:100,2]
virginica = iris_data[100:,2]

plt.plot(setosa,c='Red',marker='o',label='iris-setosa')
plt.plot(versicolor,c='Blue',marker='o',label='iris-versicolor')
plt.plot(virginica,c='Green',marker='o',label='iris-virginica')
plt.legend()
plt.title("Petal length comparison")
plt.show()
