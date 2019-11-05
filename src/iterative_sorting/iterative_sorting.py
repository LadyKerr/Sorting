# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # Divide the array into sorted & unsorted then loop thru each element
    for i in range(len(arr) - 1):
        curr_index = i
        smallest_index = curr_index
        # find the smallest element in the unsorted array
        for j in range(curr_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            # put the smallest element at the end of the sorted array
            # then swap elements
        arr[smallest_index], arr[curr_index] = arr[curr_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arr_length = len(arr) - 1  # last index in the arr
    sorted = False  # initial value of sorted is false

    while not sorted:
        sorted = True
        for i in range(0, arr_length):  # iterating thru arr
            if arr[i] > arr[i+1]:  # if num to the left is greater than num to the right
                sorted = False  # then this means the arr is not sorted and so we need to switch the nums around
                # and if this is true, then we want to assign the num to the left index of the num to the right since its a larger num
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
