"""
An Introduction to the Python debugger

Documentation: http://docs.python.org/2/library/pdb.html
"""

import numpy as np

def calc_sum(arr, slice):
    sum_result = np.sum(arr[slice])
    return sum_result

def partitioned_sum(arr, sum_every=5):
    """
    Takes an array `arr` and returns a partitioned sum in a new
    array.
    """
    idx1 = np.arange(0, len(arr), sum_every)
    idx2 = np.arange(sum_every, len(arr), sum_every)
    idx = zip(idx1, idx2)
    partitions = []
    for slices in idx:
        partitions.append(calc_sum(arr, slice(*slices)))
    return np.array(partitions)

def test_partitioned():
    np.random.seed(12345)
    arr = np.random.random(100)
    result = arr.reshape(-1, 5).sum(1)
    np.testing.assert_almost_equal(result, partitioned_sum(arr), 8)

if __name__ == "__main__":
    import numpy as np
    np.random.seed(12345)
    arr = np.random.random(100)
    print partitioned_sum(arr)

