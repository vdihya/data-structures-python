# re 1
import re
print("vidhya - RE q 1")
p = input("enter pattern to be searched: ")
f = (open(input("enter the name of the file: "), 'r'))
pattern = re.compile(p)
count = 0
for line in f:
    count = count + len(pattern.findall(line))
print(count)

# re 2
print("vidhya - RE q 2")
password = input("Enter password to test for: ")
if re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$!])[\w\d@#$]{6}$", password):
    print("match")
# (?= ... ) lookahead assertion implies that from this particular position the string starts
# \d for digits, A-Z for uppercase, a-z for lowercase, special characters
# formed my understanding of lookahead for password from this https://www.rexegg.com/regex-lookarounds.html#password
else:
    print("Not Match")

# TYL Tuples and sets 1


print("vidhya - TYL 1")


def replace(l, new):
    for x in l:
        x = x[:(len(x)-1)] + (new,)
        print(x)


replace([(10, 20, 40), (40, 50, 60), (70, 80, 90)], 200)


# TYL Tuples and sets 2

print("vidhya - TYL 2")


def sorter(listup):
    print(sorted(listup, key=lambda x: float(x[1]), reverse=True))
# this is hardcoded ... assuming the float element is the second tuple element
# not sure how to work without that assumption :/


sorter([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])

# TYL Tuples and sets 3


print("vidhya - TYL 3")


def check(str):
    if str.isalpha():
        if len(set(str.lower())) == 26:
            print("pangram")
        else:
            print("not pangram")
    else:
        print("contains non alphabetic characters, not a pangram anyway")


check(input("enter string"))

# TYL Tuples and sets 4

print("vidhya - TYL 4")


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

# TYL Tuples and sets 5
# not even close to an ideal solution but just to try a new way heh

print("vidhya - TYL 5")


def sorter(listup):
    for x in sorted(listup):
        print("minimum element:")
        print(x)
        break
    for x in sorted(listup, reverse=True):
        print("maximum element:")
        print(x)
        break


sorter({1, 2, 3, 4, 5, 62, 1234, -1, 20, 0})
