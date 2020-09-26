# arrays 1
import array as arr
ar = arr.array('I', [2, 3, 3, 3, 4])
for i in range(0, len(ar)):
    print(ar[i])
ar.append(8)
print(ar)
ar.reverse()
print(ar)
print(str(ar.itemsize))
print(str(ar.buffer_info()))

freq = 0
for i in ar:
    if (i == 3):
        freq = freq + 1
print(freq)
ar.extend(list([8, 6, 48]))
print(ar)
ar = ar + arr.array('I', [14, 15, 16])
print(ar)
ar = arr.array('I', [1]) + ar
print(ar)
ar.remove(3)
print(ar)
ar.pop(4)
print(ar)


# arrays 2

ar = arr.array('I', [1, 2, 3, 4, 34])
if len(set(ar)) == (len(ar)):
    print("false")
else:
    for i in ar:
        if(ar.count(i) > 2):
            print("true")
            break

# arrays 3
ar = arr.array('I', [23, 12, 23, 45, 56, 12])
for i in ar:
    if(ar.count(i) > 1):
        print(i)
        break
    if i == ar[len(ar)-1]:
        print(-1)
