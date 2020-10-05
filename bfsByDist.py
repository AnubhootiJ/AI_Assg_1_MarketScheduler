############### INFORMED SEARCH - BFS BY DISTANCE MATRIX #################
"""
# sample input
k = 3
m = 2
T = 2
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

# getting all user inputs
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


# getting a pair of shops with maximum distance 
mat=[]
while(change):
  for i in change:
    r=[]
    r.append(i)
    change.remove(i)
    s=0
    while(len(r)!=m):
      for j in change:
        di=get_dis(r,j)
        if s<di:
          s=di
          ele=j
      r.append(ele)
      change.remove(ele)
      s=0
    mat.append(r)


# Combining distant pairs with other pairs based on the highest similarity 
# within one single slot and highest distance among parallel slots. 
max=[]
while(mat):
  for row1 in mat:
    base=[]
    base.append(row1)
    mat.remove(row1)
    sc=0
    for par in range(k-1):
      for row2 in mat:
        s=0
        di=0
        for ro in base:
          for i in range(len(row2)):
            s+=sim[ro[i]][row2[i]]
          for i in range(len(ro)):
            for j in range(len(row2)):
              if i!=j:
                di+=d[ro[i]][row2[j]]
        score=s+C*di
        if score>sc:
          sc=score
          ro=row2
      base.append(row2)
      mat.remove(row2)
    max.append(base)


# Rearragning the final array - max in a simpler format 
# a list (m parallele slots) of list (T time slots)  of lists (one slot of k shops)
mat=[]
for row in max:
  mr=[]
  for k in range(m):
    r=[]
    for j in range(len(row)):
      r.append(row[j][k])
    mr.append(r)
  mat.append(mr)

# adding 1 to the shop number to get numbers within the range 1 to n from 0 to n-1
for i in range(T):
  for j in range(m):
    mat[i][j] = [x + 1 for x in mat[i][j]]
    
# Printing the output in the prescribed format 
# a list (m parallele slots) of list (T time slots)  of lists (one slot of k shops)   
for j in range(m):
  for i in range(T):
    if i<T-1:
      print(*mat[i][j], end=" | ")
    else:
      print(*mat[i][j], end="")
  print()
