num = input()
n = []
for i in num:
    if str(int(i)+1) in list(num):
        n.append(i)
        n.append(str(int(i)+1))

ns = sorted(list(int(x) for x in n))
if len(ns) == 4:
    if(ns[0] == ns[1]):
        print(ns)
