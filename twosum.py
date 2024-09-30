def two_sum(array, target):
    my_dict ={}
    result = []
    for index, num in enumerate(array):
        remain = target - num
        if num in my_dict:
            result.append(my_dict.get(num))
            result.append(index)
        my_dict[remain] = index
    return result
print(two_sum([7,11,15,2],9))