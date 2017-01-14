## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

plt.hist(weight_lost_a)
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a

print(mean_difference)

## 5. Permutation test ##

import numpy
mean_difference = 2.52
print(all_values)
mean_differences = []
for x in range(1000):
    group_a = []
    group_b = []
    for y in all_values:
        rand = numpy.random.rand()
        if rand >= 0.5:
            group_a.append(y)
        else:
            group_b.append(y)
    a_mean = numpy.mean(group_a)
    b_mean = numpy.mean(group_b)
    iteration_mean_difference = b_mean - a_mean
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for x in mean_differences:
    if sampling_distribution.get(x, False):
        val = sampling_distribution.get(x)
        inc = val + 1
        sampling_distribution[x] = inc
    else:
        sampling_distribution[x] = 1

## 8. P value ##

frequencies = []
for x in sampling_distribution.keys():
    if x>=2.52:
        frequencies.append(sampling_distribution.get(x))
      
p_value = numpy.sum(frequencies)/1000