# TO-DO: complete the helpe function below to merge 2 sorted arrays
# this function basically joins the split array together

# helper function to assist in joining the split arrays


def merge(left, right):
    merged_arr = []  # start with an empty array then append the left & right sides in there
    i, j = 0, 0  # this is creating an index for the left & right arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # if num on the left side is smaller or equal to the num on the right side
            merged_arr.append(left[i])  # we will add this to the left side
            i += 1  # this is incrementing the index on the left hand side since it started at 0
        else:  # if the left is larger or equal to the num on the right
            merged_arr.append(right[j])  # we will add this to the right side
            j += 1  # this is incrementing the index on the right hand side
    # putting the two arrays together
    merged_arr += left[i:]  # split into pieces so putting it all together
    merged_arr += right[j:]  # split into pieces so putting it all together
    return merged_arr  # finally we return the merged array

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = int(len(arr)/2)  # find the midpoint
    # then add nums to the left starting from the begining to the midpoint
    left = merge_sort(arr[:mid])
    # then add nums to the right starting from the midpoint to the end of the arr
    right = merge_sort(arr[mid:])
    # then using the helper function, we put the list together
    return merge(left, right)


arr = [1, 5, 9, 8, 6, 3, 15, 22, 0]
print(merge_sort(arr))
# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
