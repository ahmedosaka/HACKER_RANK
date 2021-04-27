import matplotlib.pyplot as plt
import random

population_ages = [random.randint(1,130) for c in range(0,100)]
ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages, bins,histtype='bar', rwidth=0.8)

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.show()
