sports = {
    "baseball",
    "volleyball",
    "soccer",
    "tennis",
    "football",
    "track",
    "swimming",
    "weightlifting",
    "table-tennis",
}

a1 = {"baseball", "volleyball"}
a2 = {"baseball", "soccer", "tennis"}
a3 = {"soccer", "football", "track"}
a4 = {"volleyball", "football", "swimming", "weightlifting"}
a5 = {"track", "swimming", "table-tennis"}
a6 = {"weightlifting", "table-tennis"}


def q3_verify(sports, *args):
    args_set = set()
    returned_set = set()
    for arg in args:
        args_set.update(arg)
    for i in sports:
        if i not in args_set:
            returned_set.add(i)
    if len(returned_set) > 0:
        return False
    elif len(returned_set) == 0:
        return True


# print(q3_verify(sports, a2, a3, a4, a6))


# ------ BREAK ------

raj = ["Beer", "Cat Litter"]
alanis = ["Detergent", "Beer"]
chelsea = ["Cat Litter"]


def q4_verify(*args):
    args_list = []
    for arg in args:
        for ele in arg:
            args_list.append(ele)
    args_list_len = len(args_list)
    args_set = set(args_list)
    args_set_len = len(args_set)
    if args_list_len == args_set_len:
        return True
    elif args_list_len != args_set_len:
        return False


print(q4_verify(alanis, chelsea))
