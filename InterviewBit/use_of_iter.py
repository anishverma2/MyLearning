from itertools import combinations


def imper():
    user_input = input()
    S = user_input.split()
    str_user = S[0]
    num = int(S[1])

    if 1 <= num and num <= len(str_user):
        list1 = list(combinations(str_user, num))
        for l in list1:
            user = "".join(l)
            print(user)


imper()