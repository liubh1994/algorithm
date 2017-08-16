def quick_sort(data_list, sort_flag=0):
    """
    快速排序 O(N * logN)
    :param data_list: 待排序数组
    :param sort_flag: 0: 正序 1: 逆序
    :return:
    """
    if len(data_list) < 2:
        return data_list
    if sort_flag == 1:
        mid_value = data_list[0]
        less = [i for i in data_list[1:] if i <= mid_value]
        great = [i for i in data_list[1:] if i > mid_value]
        return quick_sort(great, sort_flag) + [mid_value] + quick_sort(less, sort_flag)
    else:
        mid_value = data_list[0]
        less = [i for i in data_list[1:] if i <= mid_value]
        great = [i for i in data_list[1:] if i > mid_value]
        return quick_sort(less, sort_flag) + [mid_value] + quick_sort(great, sort_flag)


print(quick_sort([3, 2, 7, 5, 9, 10, 6]))
print(quick_sort([3, 2, 7, 5, 9, 10, 6], 1))
