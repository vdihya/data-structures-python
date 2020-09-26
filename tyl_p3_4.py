
def containstring(str1, str2):
    if(str2 in str1):
        print(str1, "contains", str2)
    else:
        print(str1, "does not contain", str2)


containstring("spartacus", "spar")
containstring("spartacus", "123")
