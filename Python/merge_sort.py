def merge_sort(data_list, sort_flag=0):
    """
    合并排序 O(N * logN)
    :param data_list: 待排序数组
    :param sort_flag: 0: 正序 1: 逆序
    :return: 有序数组
    """
    if len(data_list) < 2:
        return data_list
    mid = len(data_list)//2
    if sort_flag == 1:
        data_list[:mid] = merge_sort(data_list[:mid], sort_flag)
        data_list[mid:] = merge_sort(data_list[mid:], sort_flag)
        data_list = merge_array(data_list[:mid], data_list[mid:], sort_flag)
    else:
        data_list[:mid] = merge_sort(data_list[:mid], sort_flag)
        data_list[mid:] = merge_sort(data_list[mid:], sort_flag)
        data_list = merge_array(data_list[:mid], data_list[mid:], sort_flag)
    return data_list


def merge_array(data_list1, data_list2, sort_flag=0):
    """
    合并两个有序数组 O(N)
    :param data_list1:
    :param data_list2:
    :return: 返回合并后的数组
    """
    index1 = 0
    index2 = 0
    data_list = []
    if sort_flag == 1:
        while index1 < len(data_list1) and index2 < len(data_list2):
            if data_list1[index1] >= data_list2[index2]:
                data_list += [data_list1[index1]]
                index1 += 1
            else:
                data_list += [data_list2[index2]]
                index2 += 1
        if index1 < len(data_list1):
            data_list += data_list1[index1:]
        if index2 < len(data_list2):
            data_list += data_list2[index2:]
    else:
        while index1 < len(data_list1) and index2 < len(data_list2):
            if data_list1[index1] <= data_list2[index2]:
                data_list += [data_list1[index1]]
                index1 += 1
            else:
                data_list += [data_list2[index2]]
                index2 += 1
        if index1 < len(data_list1):
            data_list += data_list1[index1:]
        if index2 < len(data_list2):
            data_list += data_list2[index2:]
    return data_list


print(merge_sort([3, 2, 1, 6, 8, 4, 5, 10, 12, 7, 6]))
print(merge_sort([3, 2, 1, 6, 8, 4, 5, 10, 12, 7, 6], 1))

print(merge_sort([3, 2, 1, 6, 8, 4, 5, 10, 12, 7, 6, 7]))
print(merge_sort([3, 2, 1, 6, 8, 4, 5, 10, 12, 7, 6, 7], 1))
