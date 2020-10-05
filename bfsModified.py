############### INFORMED SEARCH - BFS MODIFIED #################

"""
# sample input
k = 4
m = 1
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

k = 2
m = 2
T = 1
C = 1
d=[[0,0.4,0.8,1],[0.4,0,0.6,0.7],[0.8,0.6,0,0.3],[1,0.7,0.3,0]]
"""

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


# getting a pair of shops (k shops) with highest similarity and find other pairs
# with maximum distance from that until. Repeating the process until all shops are allocated.
mat=[]
while(change):
  max = []
  for i in change:
    r=[]
    r.append(i)
    change.remove(i)
    s=0
    while(len(r)!=k):
      for j in change:
        si=get_sim(r,j) 
        if s<si: # getting the element with highest similarity
          s=si
          ele=j

      r.append(ele)
      change.remove(ele)
      s=0
    max.append(r)

    for par in range(m-1): # getting all pairs with highest distance from max 
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


# adding 1 to the shop number to get numbers within the range 1 to n from 0 to n-1
for i in range(T):
  for j in range(m):
    mat[i][j] = [x + 1 for x in mat[i][j]]


# Printing the output in the prescribed format
for i in range(m):
  for j in range(T):
    if j<T-1:
      print(*mat[j][i], end=" | ")
    else:
      print(*mat[j][i], end="")
  print()
