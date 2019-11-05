# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    index = range(0, len(arr) -1)

    for i in index:
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                if smallest_index != i:
                    arr[smallest_index], arr[i] = arr[i], arr[smallest_index]
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
