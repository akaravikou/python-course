# lower = 10
# upper = 1000000
#
# while lower < upper:
#
#     order = len(str(temp))
#     sum = 0
#     temp = lower
#
#     while temp != 0:
#         digit = temp % 10
#         sum += digit ** order
#         temp //= 10
#
#     if num == sum:
#         print(temp)


# userNumber = int(input("Enter your number: "))
# x = 2
# prime_list = []
#
# while x < userNumber:
#     prime = True
#     i = 2
#     while i < x:
#         if x % i == 0:
#             prime = False
#             break
#         i += 1
#     if prime:
#         prime_list.append(x)
#     x += 1
#
# print(f"Your prime list is: {prime_list}")


limit = 100
for digit in range(2, limit):
    for div in range(2, digit):
        if not digit % div:
            break
    else:
        print(digit)





