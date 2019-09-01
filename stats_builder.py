import statistics

sample = [-0.55, 0.0, -0.20714285714285716, -0.2, -0.4, 0.25, -0.10833333333333336, 0.5, 0.55, 0.3, 0.75, -0.45, -0.321875, -0.12, -0.5, -0.21875, 0.08499999999999999, -0.05317460317460317, 0.3333333333333333, -0.27999999999999997, 0.6, -0.09583333333333333, -0.15, -0.19999999999999998, -0.0749999999999999, 0.4, -0.0875, 0.03333333333333333, 0.6875, 0.037500000000000006, 0.049999999999999996, 0.30000000000000004, 0.2814814814814815, 0.4121428571428572, -0.04444444444444443, 0.09999999999999999, -0.16666666666666666, 0.7, 0.21428571428571427, 0.19583333333333333, 0.1861111111111111, 0.2, -0.03787878787878788, -0.14444444444444446, -0.041666666666666664, -0.75, -0.08333333333333334, 0.11499999999999999, 0.175, -0.06944444444444446, 0.24, -0.28125, -0.046666666666666676, 0.04, -0.15555555555555559, -0.08333333333333333, 0.225, -0.7142857142857143, 0.2240740740740741, -0.05000000000000001, -0.15833333333333333, -0.15590277777777778, -0.04999999999999999, 0.35, 0.1, -0.16, -0.1638095238095238, -0.18333333333333335, 0.06666666666666667, -0.01249999999999999, 0.13412698412698412, 0.05, 0.125, 0.275, 0.2441666666666667]


def polar_rounded_dictionary(full_list):
    final = []
    for i in full_list:
        i = round(i, 1)
        final.append(i)
    final = sorted(final)
    return {x: final.count(x) for x in final}


def get_deviation(numbers):
    return statistics.pstdev(numbers)


def get_average(numbers):
    return statistics.mean(numbers)





