def check(str1, sub):
    while len(str1) > 0:
        index = str1.find(sub)

        if index == -1:
            break  # substring not found in string
        str1 = str1.replace(sub, "", 1)

    if(len(str1) == 0):
        print("empty string obtained")
    else:
        print("empty string not obtainable")


check("sparspar", "spar")
