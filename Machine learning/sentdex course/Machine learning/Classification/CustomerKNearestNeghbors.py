import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')
from scipy.spatial import distance

dataset = {'k': [[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]


# [[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
# plt.scatter(new_features[0], new_features[1], s=100)
# plt.show()


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warning.warn('K is set to a value less than total voting groups!')
    distances=[]
    for group in data:
        print('group', group)
        for features in data[group]:
            print('features',features)
            euclidean_distance = distance.euclidean(features, predict)
            print('euclidean_distance', euclidean_distance)
            distances.append([euclidean_distance, group])
            print('distances',distances)
    votes= [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)


[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], s=100, color=result)
plt.show()
