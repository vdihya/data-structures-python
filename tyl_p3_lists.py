from itertools import permutations
print("1. Write a Python program to get the largest number from a list.\n")


def max_in_list(list):
    return max(list)


print(max_in_list([1, 23, 199, -11, 2456]))

print("2. Write a Python program to remove duplicates from a list.\n")


def remove_duplicates(ulist):
    # convert the list into a keys by giving list items as keys, this eliminates duplicate keys
    return list(dict.fromkeys(ulist))  # return reconverted list


print(remove_duplicates([1, 1, 1, 2, 4, 5, 1, 2, 1, 2, 2]))

print("3. Write a Python function that takes two lists and returns True if they have at least one common member.\n")


def common_list(list1, list2):
    flag = 1
    list1.sort()
    list2.sort()
    for i in list1:
        for j in list2:
            if(i == j):
                flag = 0
                print("common member")
                return

    if(flag == 1):
        print("no common member")


common_list([1, 2, 3], [5, 5, 7])
common_list([1, 2, 3], [2, 5, 7])


print("4. Write a Python program to print the numbers of a specified list after removing even numbers from it.\n")


def remove_even(ilist):
    for i in ilist:
        if(not i % 2):
            ilist.remove(i)
    return ilist


print(remove_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("5. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).\n")


def print_squares():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])


print_squares()

print("6. Write a Python program to generate all permutations of a list in Python.\n")


def permutations_of_list(list):
    for i in permutations(list):
        print(i)


permutations_of_list([9, 0, 5])

print(" 7.   Write a Python program to append a list to the second list.\n")


def append_second_list(list1, list2):
    for i in list2:
        list1.append(i)
    return list1


print(append_second_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

print("8.   Write a Python program to get the frequency of the elements in a list.\n")


def frequency_elements(ilist):
    freq = {}
    for i in ilist:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))


frequency_elements([1, 2, 3, 1, 3, 41, 3, 41, 3, 1, 2, 40])

print("9. Write a python program to count the number of vowels and consonants in a file.\n")


def count_letters():
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowels = 0
    consonants = 0

    f = open("letters.txt", 'r')
    while 1:
        char = f.read(1)
        if(char in vowel):
            vowels = vowels + 1
        elif not char:
            break
        else:
            consonants = consonants + 1
    print("vowels: %d " % vowels)
    print("consonants: %d " % consonants)


count_letters()

print("10. Write a program in python to print the file contents with line number using file.\n")


def print_line():
    with open('lines.txt', 'r') as f:
        lines = 1
        for line in f:
            print("%d. %s" % ((lines), line))
            lines = lines + 1


print_line()
