def reverseArray(array):
    """Reverse elements of the array in place

    :param array: list of values to reverse in place
    :return: None
    """
    for i in xrange(len(array) // 2):
        otherIdx = len(array) - i - 1
        currentVal = array[i]
        array[i] = array[otherIdx]
        array[otherIdx] = currentVal


