import numpy as np


def convert_two_1_d_arrays_into_2_d_array(arr1, arr2):
    """
    convert two array of 1 D to 1 array with 2D, the array must to be at the same size otherwise raise exception.
    :param arr1: Numpy array 1D
    :param arr2: Numpy array 1D
    :return: Numpy array 2D
    """
    if arr1.size == arr2.size:
        return np.dstack((arr1, arr2))
    else:
        raise Exception


if __name__ == '__main__':
    try:
        a = np.array([[1], [2], [3], [4]])
        b = np.array([[5], [6], [7], [8]])
        print(convert_two_1_d_arrays_into_2_d_array(a, b))
        print("_" * 30)

        c = np.array([[1], [2], [3], [4], [9]])
        d = np.array([[5], [6], [7], [8]])
        print(convert_two_1_d_arrays_into_2_d_array(c, d))
    except Exception:
        print("Array size isn't the same")


