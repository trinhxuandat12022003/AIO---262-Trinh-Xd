'''
Chương trình cho I.1
'''


def max_kernel(num_list, k):
    result = []
    for i in range(0, len(num_list) - k + 1):
        kernel = num_list[i: i + k]
        result.append(max(kernel))
    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
