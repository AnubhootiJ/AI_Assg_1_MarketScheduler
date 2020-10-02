# m market places (that can run in parallel) in T slots with K shops in 1 market place
"""
k = 1
m = 2
T = 3
C = 1
d=[[0,0.4,0.8,1,0.8,1],
   [0.4,0,0.6,0.7,0.8,1],
   [0.8,0.6,0,0.3,0.8,1],
   [1,0.7,0.3,0,0.8,1],
   [0.8,0.6,0,0.3,0,1],
   [0.4,0.6,0,0.3,1,0]]

k = 2
m = 2
T = 1
C = 1
d=[[0,0.4,0.8,1],[0.4,0,0.6,0.7],[0.8,0.6,0,0.3],[1,0.7,0.3,0]]
"""

k = 2
m = 2
T = 3
C = 1
d = [[0, 0.0, 0.8, 0.9, 0.2, 0.1, 1.0, 0.8, 0.2, 0.3, 0.8, 0.8],
     [0.0, 0, 0.8, 1.0, 0.2, 0.1, 0.8, 0.9, 0.2, 0.2, 0.8, 1.0],
     [0.8, 0.8, 0, 0.1, 0.8, 0.9, 0.2, 0.2, 0.7, 0.9, 0.0, 0.2],
     [0.9, 1.0, 0.1, 0, 0.7, 0.9, 0.0, 0.2, 0.9, 0.9, 0.1, 0.1],
     [0.2, 0.2, 0.8, 0.7, 0, 0.1, 0.8, 1.0, 0.3, 0.2, 0.9, 0.7],
     [0.1, 0.1, 0.9, 0.9, 0.1, 0, 0.8, 0.9, 0.1, 0.2, 0.8, 0.9],
     [1.0, 0.8, 0.2, 0.0, 0.8, 0.8, 0, 0.0, 0.9, 0.8, 0.1, 0.0],
     [0.8, 0.9, 0.2, 0.2, 1.0, 0.9, 0.0, 0, 0.8, 0.9, 0.2, 0.0],
     [0.2, 0.2, 0.7, 0.9, 0.3, 0.1, 0.9, 0.8, 0, 0.2, 0.8, 0.8],
     [0.3, 0.2, 0.9, 0.9, 0.2, 0.2, 0.8, 0.9, 0.2, 0, 0.8, 0.9],
     [0.8, 0.8, 0.0, 0.1, 0.9, 0.8, 0.1, 0.2, 0.8, 0.8, 0, 0.3],
     [0.8, 1.0, 0.2, 0.1, 0.7, 0.9, 0.0, 0.0, 0.8, 0.9, 0.3, 0]]


# computing the similarity matrix
sim = []
for i in range(k * m * T):
    row = []
    for j in range(k * m * T):
        r = 1 - d[i][j]
        r = round(r, 2)
        row.append(r)
    sim.append(row)


# computing maximum possible goodness without considering Time slots
def max_good(row):
    g = 0
    dif = 0
    # Computing max similarity not considering time slot division
    for i in range(m):
        for x in range(T * k):
            for j in range(x + 1, T * k):
                g = g + sim[row[i][x]][row[i][j]]
    # Computing max distance not considering time slot division
    for x in range(T * k):
        for i in range(m):
            for j in range(i + 1, m):
                for ro in range(T * k):
                    dif = dif + d[row[i][x]][row[j][ro]]
    g = g + C * dif
    g = round(g, 3)
    return g


# Getting similarity for a given row of list
def get_sim(ar):
    s = 0
    for ro in ar:
        for i in range(len(ro)):
            for j in range(i + 1, len(ro)):
                s = s + sim[ro[i]][ro[j]]
    return s


# Getting distance between two rows of a list
def get_ds(l, ar):
    sc = 0
    if T == 1:
        for s in l:
            for t in ar:
                sc = sc + d[s][t]
        return sc
    else:
        for to in l:
            for i in range(len(to)):
                for h in to[i]:
                    for x in ar[i]:
                        sc = sc + d[h][x]
        sc = C * sc
    return sc


# getting all subsets (given length of the subset) of a given list
def getpair(pair, nodes, i, nu, T):

    # storing a subset pair once it reaches the required length
    if i == T * k:
        data = list(range(T * k))
        for x in range(T * k):
            data[x] = row[x]
        pair.append(data)
        # print(lst)
        return

    # checking if the whole list of nodes is traversed
    if nodes >= len(nu):
        return

    # Doing recursion with 1 adding the current element in subset list and 1 not adding it in the subset list
    # This consider all possible case for an element - that is, it can either be in the subset or it can't be
    row[i] = nu[nodes]
    getpair(pair, nodes + 1, i + 1, nu, T)
    getpair(pair, nodes + 1, i, nu, T)


# getting all possible pairs based on T,m and k
def pairs(m, lst, T):
    pair = []
    pair2 = []
    final = []
    fin = lst

    # getting all possible pairs after all shops are divided in parallel slots (that is, divided by m)
    getpair(pair, 0, 0, lst, T)

    # Getting remaining shops for each subset and appending it to data.
    for ro in pair:
        data = []
        for r in fin:
            if r not in ro:
                data.append(r)
        # Further dividing the remaining shops in parallel slots
        lst = data
        getpair(pair2, 0, 0, lst, T)

        # Appending the pairs to previous subsets, creating all possible combinations for a division
        for s in pair2:
            final.append([ro, s])
        pair2 = []

    # only 1 division happened
    # the process will continue for m-2 times
    if m > 2:
        for w in range(m - 2):
            final2 = []

            # Getting remaining shops in each row of subsets
            for ro in final:
                data2 = []
                data = []
                for s in fin:
                    for r in ro:
                        if s in r:
                            data2.append(s)
                for s in fin:
                    if s not in data2:
                        data.append(s)

                # getting all possible subsets for remaining shops
                lst = data
                getpair(pair2, 0, 0, lst, T)
                # Appending it to create all possible combinations
                for s in pair2:
                    ar = []
                    for r in ro:
                        ar.append(r)
                    ar.append(s)
                    final2.append(ar)
                pair2 = []
            final = final2
            final2 = []

    # Function returning the final array containing all possible combinations after m divisions
    return final


# Initializing required variables
good = 0
lst = []
row = list(range(T * k))  # Initializing the list of all shops
for x in range(m * T * k):
    lst.append(x)

# checking for naive/basic conditions
# only 1 shop, returns 1 shop as the answer
if m == 1 and k == 1 and T == 1:
    print("1")

# Division when only Time slots given
elif m == 1 and k == 1:
    for i in lst:
        print(i + 1, end="|")

# Division when only parallel markets given
elif k == 1 and T == 1:
    for i in lst:
        print(i + 1)

# The rest of the conditions
else:
    # Computing goodness for all pairs and return the optimal pair
    # Dividing on basis of parallel shops (m) first
    if m > 1:
        final = pairs(m, lst, T)  # getting possible combinations after dividing shops in m parallel slots

        # Checking max possible goodness for each possible combination
        # The combination with highest value is retained
        for row in final:
            r = max_good(row)
            if good < r:
                good = r
                show = row
        if T > 1:
            final2 = pairs(T, show[0], 1)
    else:
        if T > 1:
            final2 = pairs(T, lst, 1)

    # Dividing in pairs on basis of time slots
    if T > 1:
        sc = 0
        if k > 1:
            for line in final2:
                r = get_sim(line)  # getting similarity unction to create optimal set
                if r > sc:
                    sc = r
                    fin = [line]
        elif k == 1:
            fin = [final2[0]]

        if m > 1:
            for i in range(len(show) - 1):
                final = pairs(T, show[i + 1], 1)
                st = 0
                for line in final:
                    # Getting goodness for each pair
                    s = sc + get_sim(line)
                    r = get_ds(fin, line)
                    if s + r > st:
                        st = s + r
                        lo = line
                fin.append(lo)  # retaining the comination with highest value
                sc = st
            show = fin  # getting the final combination divided into m parallel and T time slots
    # Special case if only 1 time slot available
    elif T == 1:
        r = 0
        dif = 0
        for se in show:
            for i in range(len(se)):
                for j in range(i + 1, len(se)):
                    r = r + sim[se[i]][se[j]]

        for i in range(len(show)):
            for j in range(i + 1, len(show)):
                dif = dif + get_ds(show[i], show[j])

        sc = r + C * dif

    # The final goodness score
    sc = round(sc, 2)

    # Preparing resultant set for printing final output
    if m == 1:
        show = fin

    # Adjusting the shop values by adding 1 to it
    for i in range(m):
        for j in range(T):
            if T > 1:
                show[i][j] = [x + 1 for x in show[i][j]]

    # Printing output by separating k shops by space in T time slots by |
    # m Parallel shops are divided by a line
    for i in range(m):
        for j in range(T):
            if T > 1:
                print(*show[i][j], end=" | ")
            else:
                print(*show[i], end="")
        print()
    # print(sc)
