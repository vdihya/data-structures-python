from itertools import permutations
# the easiest method is to sort both strings, but this is another approach


def anagram(str1, str2):
    flag = 1
    for item in permutations(str1):
        if(("".join(item)) == (str2)):
            flag = 0
            break
    if(flag == 1):
        print("not anagrams")
    else:
        print("anagrams!")


anagram("rasp", "spar")
