import numpy as np
import matplotlib.pyplot as plt


def compute_the_x_and_y_coordinates(start, end):
    """
    The function get start and end *np.pi range. using matplotlib to show the graph.
    :param start:(int) Start range.
    :param end:(int) End range.
    """
    x = np.arange(start, end * np.pi, 0.2)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    compute_the_x_and_y_coordinates(2, 5)


