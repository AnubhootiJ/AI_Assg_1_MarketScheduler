import random

# getting the input from users
k = int(input())
m=int(input())
T=int(input())
C=float(input())

n = m*T*k
d=[]
for i in range(n):
  r = list(map(float, input().split())) 
  d.append(r)

# computing the similarity matrix 
sim = []

for i in range(n):
  row = []
  for j in range(n):
      r = 1 - d[i][j]
      r = round(r, 2)
      row.append(r)
  sim.append(row)


# function for calculating similarity between a list and a shop number
def get_sim(lst,el):
  s=0
  for i in lst:
    s+=sim[i][el]
  return s

# function for calculating distance between shops in a list and a shop number
def get_dis(lst,el):
  s=0
  for i in lst:
    s+=d[i][el]
  return C*s

# function for getting similarity between shops within 1 slot
def get_s(lst):
  s=0
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      s+=sim[lst[i]][lst[j]]
  return s

# function for getting distance between shops within 2 slots
def get_d(lst,lst2):
  di=0
  for el in lst:
    for el2 in lst2:
      di+=d[el][el2]
  return C*di

# function for computing the goodness function for a given list (m parallel shops) 
# of lists (T time slots) of lists (K shops)
def goodness(lst):
  si=0
  for row in lst:
    for i in range(len(row)):
      si+=get_s(row[i])
      for j in range(i+1,len(row)):
        si+=get_d(row[i],row[j])
  return round(si,2)

# function for getting the schedule starting with a shop at random 
# takes list of all shops as the input
def get_schedule(change):
  mat=[]
  while(change):
    max = []
    i = random.choice(change)
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

    for par in range(m-1):
      di=[]
      while(len(di)!=k):
        maxd=0
        for j in change:
          dis=0
          for row in max:
            dis+= get_dis(row,j)
          if di:
            dis+=get_sim(di,j)
          if dis>maxd:
            maxd=dis
            ele2=j
        di.append(ele2)
        change.remove(ele2)
        maxd=0
      max.append(di)
      
    mat.append(max)
    max=[]
  return mat

# initializing the list of ships and giving an iteration of 10
# i.e, we will compute and compare 10 schedules returning the one with highest goodness score
lst=[]
iterate =10
for i in range(iterate):
  for j in range(n):
    lst.append(j)
  good=0
  fin=get_schedule(lst)
  g=goodness(fin)
  if g>good:
    good=g
    mat=fin

# adding 1 to the shop number to get numbers within the range 1 to n from 0 to n-1
for i in range(T):
  for j in range(m):
    mat[i][j] = [x + 1 for x in mat[i][j]]


# Printing the output in the prescribed format
# a list (m parallel slots) of list (T time slots)  of lists (one slot of k shops)
for i in range(m):
  for j in range(T):
    if j<T-1:
      print(*mat[j][i], end=" | ")
    else:
      print(*mat[j][i], end="")
  print()
  
