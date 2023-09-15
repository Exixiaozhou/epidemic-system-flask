import time
import numpy as np


def random_color(number):
    """ 随机颜色生成 """
    color_list = list()
    num_list = [str(x) for x in np.arange(10)]
    alphabet = [chr(x) for x in (np.arange(6) + ord('A'))]
    color_arr = np.hstack((num_list, alphabet))
    for j in range(number):
        color_single = '#'
        for i in range(6):
            index = np.random.randint(len(color_arr))
            color_single += color_arr[index]
        color_list.append(color_single)
    return color_list
