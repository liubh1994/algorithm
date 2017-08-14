def select_sort(data_array, sort_flag=0):
    """
    选择排序 O(N^2)
    :param data_array: 待排序数组
    :param sort_flag: 0: 正序 1: 逆序
    :return: 排序后的数组
    """
    if len(data_array) <= 1:
        return data_array
    if sort_flag == 1:
        for out_index in range(0, len(data_array)):
            max_value = data_array[out_index]
            index = out_index
            sorted_flag = True
            for in_index in range(out_index, len(data_array)):
                if data_array[in_index] > max_value:
                    max_value = data_array[in_index]
                    index = in_index
                    sorted_flag = False
            if sorted_flag is True:
                continue
            if index != out_index:
                data_array[index] = data_array[out_index]
                data_array[out_index] = max_value
    else:
        for out_index in range(0, len(data_array)):
            min_value = data_array[out_index]
            index = out_index
            sorted_flag = True
            for in_index in range(out_index, len(data_array)):
                if data_array[in_index] < min_value:
                    min_value = data_array[in_index]
                    index = in_index
                    sorted_flag = False
            if sorted_flag is True:
                continue
            if index != out_index:
                data_array[index] = data_array[out_index]
                data_array[out_index] = min_value
    return data_array


def pop_sort(data_array, sort_flag=0):
    """
    冒泡排序 O(N^2)
    :param data_array: 待排序数组
    :param sort_flag: 0: 正序 1: 逆序
    :return: 排序好的数组
    """
    if len(data_array) <= 1:
        return data_array
    if sort_flag == 1:
        for out_index in range(0, len(data_array)-1):
            sorted_flag = True
            for in_index in range(0, len(data_array)-out_index-1):
                if data_array[in_index] < data_array[in_index+1]:
                    tmp_value = data_array[in_index]
                    data_array[in_index] = data_array[in_index+1]
                    data_array[in_index+1] = tmp_value
                    sorted_flag = False
            if sorted_flag is True:
                break
    else:
        for out_index in range(0, len(data_array)-1):
            sorted_flag = True
            for in_index in range(0, len(data_array)-out_index-1):
                if data_array[in_index] > data_array[in_index+1]:
                    tmp_value = data_array[in_index]
                    data_array[in_index] = data_array[in_index+1]
                    data_array[in_index+1] = tmp_value
                    sorted_flag = False
            if sorted_flag is True:
                break
    return data_array


print(select_sort([1, 3, 2, 7, 5, 8, 9]))
print(select_sort([1, 3, 2, 7, 5, 8, 9], 1))
print(select_sort([1, 3, 2, 7, 5, 8, 9], 0))
print(select_sort([]))
print(select_sort([1]))

print(pop_sort([1, 3, 2, 7, 5, 8, 9]))
print(pop_sort([1, 3, 2, 7, 5, 8, 9], 1))
print(pop_sort([1, 3, 2, 7, 5, 8, 9], 0))
print(pop_sort([]))
print(pop_sort([1]))
