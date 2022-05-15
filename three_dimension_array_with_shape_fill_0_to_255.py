import numpy as np


def three_dimension_array_with_shape_fill_0_to_255():
    """
    
    :return:
    """
    np.random.seed(32)
    return np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)


if __name__ == '__main__':
    print(three_dimension_array_with_shape_fill_0_to_255())
