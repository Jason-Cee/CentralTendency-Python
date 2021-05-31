# import numpy
# from scipy import stats
#
# test_scores = [12, 99, 86, 87, 88, 45, 87, 94, 78, 77, 85, 86]
# my_mean = numpy.mean(test_scores)
# my_mode = stats.mode(test_scores)
# my_range = numpy.ptp(test_scores)
# my_median = numpy.median(test_scores)
# x = numpy.percentile(test_scores, 75)
# x = numpy.var(test_scores)
# my_std = numpy.std(test_scores)
#
# print("The mean is: ", my_mean)
# print("The median is: ", my_median)
# print("The mode is: ", my_mode)
# print("The range is: ", my_range)
# print("The 75% percentile for the marks is: ", x)
# print("The variance of the marks is: ", x)
# print("The standard deviation is: ", my_std)

import matplotlib.pyplot as plt

cities = ['East London', 'Cape Town', 'Kimberley', 'Durban']
rainfall = [140, 200, 120, 157]
x_pos = [i for i, _ in enumerate(cities)]  # labels on the x-axis
# labeling and visuals
plt.bar(x_pos, rainfall, color='green')
plt.xlabel("cities")
plt.ylabel("Rainfall in (mm)")
plt.title("Rainfall for the 4 main cities in SA")
plt.xticks(x_pos, cities)
plt.show()
