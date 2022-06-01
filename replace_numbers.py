import numpy as np


def replace_numbers(num, operation, array, replace_num):
    """
    Get array and replace the values by replace_num if the give 'operation'(< or > or ==) comparison to num.
    :param num:(int)
    :param operation:(string)  Command: < or > or ==
    :param array:(array) Given np array.
    :param replace_num:(int)
    :return:Array after replace values by the wanted operation.
    """
    print("Array before replace values by: " + operation)
    print(array)
    if operation == ">":
        array[array > num] = replace_num
    elif operation == "<":
        array[array < num] = replace_num
    elif operation == "==":
        array[array == num] = replace_num
    print("Array After replace values by: " + operation)
    print(array)
    return array


if __name__ == '__main__':
    replace_numbers(10, "<", np.random.randint(20, size=10), -1)
    print("-"*30)
    replace_numbers(10, ">", np.random.randint(20, size=10), -1)
    print("-"*30)
    replace_numbers(10, "==", np.random.randint(20, size=10), -1)
