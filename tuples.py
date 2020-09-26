# 1
with open((input("Enter a file name: ")), "r") as fi:
    fromlist = []
    freq = {}
    for ln in fi:
        if ln.startswith("From "):
            fromlist.append(ln[5:].split(' ')[0])

    for item in fromlist:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% s : % d" % (key, value))

sortedl = sorted(freq.items(), key=lambda x: x[1])[0]
print("The person with the least commits is %s" % sortedl[0])
sortedl = sorted(freq.items(), key=lambda x: x[1], reverse=True)[0]
print("The person with the most commits is %s" % sortedl[0])

# 2
with open((input("Enter a file name: ")), "r") as fi:
    timestamps = []
    freq1 = {}
    for ln in fi:
        if ln.startswith("From "):
            print(ln.split(':')[0][-2:])
            timestamps.append(ln.split(':')[0][-2:])
    for item in timestamps:
        if (item in freq1):
            freq1[item] += 1
        else:
            freq1[item] = 1

    for key, value in sorted(freq1.items()):
        print("% s : % d" % (key, value))
# 3
fname = input("Enter a file name: ")
fhand = open(fname, 'r')
words = fhand.read()

words = words.lower()
freq2 = {}
letters = list()
for i in words:
    if i.isalpha() == True:
        letters.append(i)
for item in letters:
    if (item in freq2):
        freq2[item] += 1
    else:
        freq2[item] = 1

for key, value in sorted(freq2.items(), key=lambda x: x[1], reverse=True):
    print("% s : % d" % (key, value))


# tyl1

stock = {}
prices = {}


def create_list(listofkeyvals):
    dict_ = {}
    length = len(listofkeyvals)
    for i in range(0, (int)(length/2)):
        dict_[listofkeyvals[i]] = listofkeyvals[(int)(length/2)+i]

    return dict_


def display(kkey):
    print("\n\nItem :  Stock :  Price\n")
    print("% s : %d : % d" % (kkey, stock[kkey], prices[kkey]))


def compute_bill(purchases):
    total = 0
    for i in purchases:
        if stock[i] > 0:
            total = total + prices[i]
            stock[i] = stock[i]-1

    return total


def if_all_sold(item):
    if stock[item] == 0:
        return ("Yes there is still stock of %s" % item)
    else:
        return ("No there is no stock of %s" % item)


def max_stock():
    print("Maximum stocked item:")
    print(sorted(stock.items(), key=lambda x: x[1], reverse=True)[0])


def max_price():
    print("Maximum priced item:")
    print(sorted(prices.items(), key=lambda x: x[1], reverse=True)[0])


stock = (create_list(['radish', 'apple', 'tomato', 5, 2, 3]))
prices = create_list(['radish', 'apple', 'tomato', 50, 100, 30])
display('radish')
print("Total cost of purchases: %d" % compute_bill(['apple', 'apple']))
print(if_all_sold('apple'))
max_stock()
max_price()

# tyl 2
d = {'match1': {'player1': 57, 'player2': 38},
     'match2': {'player3': 9, 'player1': 42},
     'match3': {'player2': 41, 'player4': 63, 'player3': 91}
     }


def highestscore(d):
    totalscore = dict()
    for match in d:
        for plr in d[match]:
            if plr in totalscore:  # if player exists in totalscore dict add his score else create a score dictionary entry for that player
                # access score in the nested dictionary
                totalscore[plr] += d[match][plr]
            else:
                totalscore[plr] = d[match][plr]

    # how did i arrive at this logic?? i truly cannot understand the logic in indexing so i decided to experiment:
    print(totalscore)
    print(totalscore.items())
    print(sorted(totalscore, key=lambda x: x[1], reverse=True))
    print(sorted(totalscore.items(), key=lambda x: x[1], reverse=True)) 
    # print(totalscore.items()) = a dictionary that is a list of tuples
    # print(sorted(totalscore, key=lambda x: x[1], reverse=True)) = only sorts keys, unfortunately this is not indexable(?)
    # print(sorted(totalscore.items(), key=lambda x: x[1], reverse=True)) = sorts list of tuples

    best = (sorted(totalscore.items(), key=lambda x: x[1], reverse=True))[
        0][0]  # this gives zeroth tuple in the list, zeroth element of that tuple = key of max player
    return best, totalscore[best]


print("playername, score of player: ")
print(highestscore(d))


# tyl 3

inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}


def change(inventory):
    inventory['pocket'] = ['seashell', 'strange berry', 'lint']
    print(sorted(inventory['backpack']))
    del inventory['backpack'][inventory['backpack'].index('dagger')]
    inventory['gold'] = inventory['gold'] + 50

    print(inventory)


change(inventory)
