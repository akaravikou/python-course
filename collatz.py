# limit = 10 ** 4
# result = {1 : 0}
# current_digit = 2
#
# while current_digit < limit:
#     copy_digit = current_digit
#     current_steps = 0
#     GO = True
#     while GO:
#         if copy_digit % 2:
#             copy_digit = (3 * copy_digit + 1) // 2
#             current_steps += 2
#         else:
#             copy_digit //= 2
#             current_steps += 1
#         if copy_digit in result:
#             result[current_digit] = current_steps + result[copy_digit]
#             GO = False
#     current_digit += 1
# key = max(result, key=result.get)
# key, result[key]
