import numpy as np


def evenly_distributed_5_50():
    """
    Create vector with evenly_distributed between 5 - 50 using  numpy linspace function.
    :return:Evenly_distributed vector.
    """
    vec = np.linspace(5, 50, 10)
    return vec


if __name__ == '__main__':
    print(evenly_distributed_5_50())
