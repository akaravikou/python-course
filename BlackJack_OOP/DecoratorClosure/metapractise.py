# l = ["One apple", "Cost amount about 1000$", "general Samsung", "Oh my Godness"]
#
#
# def has_name(words):
#     global var
#     for word in words:
#         var = "samsung" in word
#     return var
#
#
# n1 = bool(filter(has_name, l))
# print(n1)


def add(*args):
    print(args)
    print(sum(args))


add(1, 2, 3)

l = [1, 3, 4]
add(*l)