import matplotlib.pyplot as plt
import csv
import numpy as np


# Part One
# x = []
# y = []

# with open('example.txt', 'r') as csvfile:
#     plots= csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         # print(row)
#         # print(row[0])
#         # print(row[1])
#         x.append(int(row[0]))
#         y.append(int(row[1]))

# plt.plot(x,y, label='loaded from file!')


x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()