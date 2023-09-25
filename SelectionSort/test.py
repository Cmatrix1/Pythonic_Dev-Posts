

def get_lower_cnt(lst):
    low = lst[0]
    for i in lst:
        if i < low:
            low = i
    return low

print(get_lower_cnt([1, 2, 3, 4, 5, -189]))



def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
