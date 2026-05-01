# def same_parity_filter(coll: list) -> list[int]:
#     if not coll:
#         return []
#     result = []
#     parity = 'even' if coll[0] % 2 == 0 else 'odd'
#     for num in coll:
#         if parity == 'even':
#             if num % 2 == 0:
#                 result.append(num)
#         else:
#             if num % 2 != 0:
#                 result.append(num)
#     return result

def is_even(number: int) -> bool:
    return number % 2 == 0

def same_parity_filter(coll: list) -> list:
    if not coll:
        return []
    first_num_parity = is_even(coll[0])
    filtered_nums = filter(lambda num: is_even(num) == first_num_parity, coll)
    return list(filtered_nums)


print(same_parity_filter([2, 0, 1, -3, 10, -2]))
