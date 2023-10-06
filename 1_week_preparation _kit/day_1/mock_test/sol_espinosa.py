
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # Write your code here
    sorted_arr = arr
    sorted_arr.sort()

    len_arr = len(sorted_arr)

    middle = (len_arr // 2)

    return sorted_arr[middle]
