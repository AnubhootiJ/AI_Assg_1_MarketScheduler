################## INFORMED SEARCH - BFS ######################

"""
# sample input
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

n = m*T*k

"""

# getting all the user inputs
k = int(input())
m=int(input())
T=int(input())
C=float(input())

n = m*T*k
d=[]
for i in range(n):
  r = list(map(float, input().split())) 
  d.append(r)


# initializing the list of shops with shop number 
# also, computing the similarity matrix 
sim = []
lst=[]
change=[]
for i in range(n):
  lst.append(i)
  change.append(i)
  row = []
  for j in range(n):
      r = 1 - d[i][j]
      r = round(r, 2)
      row.append(r)
  sim.append(row)


# function for calculating similarity between a list and a shop number
def get_sim(lst,r):
  si = 0
  for i in lst:
    si = si+sim[i][r]
  return si

# function for calculating distance between shops in a list and a shop number
def get_dis(mat,lst2):
  dis = 0
  for row in mat:
    for i in row:
      for j in lst2:
        dis+= d[i][j]

  dis = C*dis # multiplying the coefficient with the distance 
  return dis


# pairing the shops with maximum similarity
# storing all the pairs in the max list
# every pair has k elements
max = []
while(change):
  for i in change:
    r=[]
    r.append(i)
    change.remove(i)
    s=0
    while(len(r)!=k):
      for j in change:
        si=get_sim(r,j)
        if s<si:
          s=si
          ele=j
      r.append(ele)
      change.remove(ele)
      s=0
    max.append(r)


# clubbing the pairs with maximum distance between them
# m pairs are clubbed together
mdiv=[]
while(max):
  for row1 in max:
    div=[]
    max_d=0
    div.append(row1)
    max.remove(row1)
    while(len(div)!=m):
      for row2 in max:
        dis = get_dis(max,row2)
        if dis>max_d:
          max_d=dis
          max_el=row2
      div.append(row2)
      max.remove(row2)
      max_d=0
    mdiv.append(div)


# adding 1 to the shop number to get numbers within the range 1 to n from 0 to n-1
for i in range(T):
  for j in range(m):
    mdiv[i][j] = [x + 1 for x in mdiv[i][j]]


# Printing the output in the prescribed format
for i in range(m):
  for j in range(T):
    if j<T-1:
      print(*mdiv[j][i], end=" | ")
    else:
      print(*mdiv[j][i], end="")
  print()
