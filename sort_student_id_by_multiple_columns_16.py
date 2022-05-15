import numpy as np


def sort_student_id_by_multiple_columns(ids, heights):
    """
    Sort the student id with increasing height of the students from given students id and height. Print the integer
        indices that describes the sort order by multiple columns and the sorted data.
    :param ids: Numpy array of students id.
    :param heights: Numpy array of students height.
    """
    indices = np.lexsort((ids, heights))
    print("Sorted indices:")
    print(indices)
    print("Sorted data:")
    for i in indices:
        print(ids[i], heights[i])


if __name__ == '__main__':
    student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
    sort_student_id_by_multiple_columns(student_id, student_height)
