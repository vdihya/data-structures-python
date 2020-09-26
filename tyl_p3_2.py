from itertools import permutations


def permute(str):
    for item in permutations(str):
        print(item)  # print as letters in a string
        print("".join(item))  # print as a whole string


permute(input("enter a string to find the permutations of: "))
