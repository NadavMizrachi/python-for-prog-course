def is_mono_b_direct(li):
    return not {False, True}.issubset(set([(li[i] <= li[i + 1]) for i in range(0, len(li) - 1)]))

    # return len(set([(li[i] <= li[i + 1]) for i in range(0, len(li) - 1)])) <= 1
    # return all([(li[i] <= li[i + 1]) for i in range(0, len(li) - 1)]) or \
    #        all([(li[i] >= li[i + 1]) for i in range(0, len(li) - 1)])


print(is_mono_b_direct([1,3,4,6]))

print(is_mono_b_direct([51,23,14,6]))

print(is_mono_b_direct([51,3,14,6]))

print(is_mono_b_direct([]))

# li = [1, 2, 3]
# res = len(set([(li[i] <= li[i + 1]) for i in range(0, len(li) - 1)])) <= 1
#
# print(res)