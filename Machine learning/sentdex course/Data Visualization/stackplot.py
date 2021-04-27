import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping=[7,8,9,12,6]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

plt.stackplot(days, sleeping,eating,working,playing, colors=['r','m','k','c'])
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()
plt.show()
