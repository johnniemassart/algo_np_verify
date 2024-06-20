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


print(q3_verify(sports, a2, a3, a4, a6))
