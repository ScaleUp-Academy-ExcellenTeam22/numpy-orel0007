import numpy as np


def count_the_number_of_days_of_specific_month(date1, date2):
    """
    Count the number of days of specific month by using np.datetime64.
    :param date1:(string) End date
    :param date2:(string) Start date
    :return: Number of days between date1 - date2.
    """
    return np.datetime64(date1) - np.datetime64(date2)


if __name__ == '__main__':
    print("Number of days, February, 2016: ")
    print(count_the_number_of_days_of_specific_month('2016-03-01', '2016-02-01'))
    print("Number of days, February, 2017: ")
    print(count_the_number_of_days_of_specific_month('2017-03-01', '2017-02-01'))
    print("Number of days, February, 2018: ")
    print(count_the_number_of_days_of_specific_month('2018-03-01', '2018-02-01'))
