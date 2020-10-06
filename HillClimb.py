#################### HILL CLIMB WITH RANDOM RESTARTS #################

import random

####################inputs#################

k = int(input())
m=int(input())
T=int(input())
C=float(input())

n = m*T*k
d=[]
for i in range(n):
  r = list(map(float, input().split())) 
  d.append(r)

################variables initiation##############
schedule=[]
s=[]

local_result_schedule = []
global_result_schedule= []

global_optimal_goodness= 0.0
local_optimal_goodness= 0.0

num_restart = 1000
num_climb = 100

##creating a list of all shops## 
random_list= [] 
for i in range(m*k*T):
  random_list.append(i)


#######calculating s matrix###############
for i in range(k*m*T):
    row=[]
    for j in range(k*m*T):
        r = 1-d[i][j]
        r = round(r,2)
        row.append(r)
    s.append(row)



#########functions#############
def random_restart() :  
  random.shuffle(random_list)            
  i=0
  random_schedule =[]
  for c1 in range(m) :
    list2= []
    for c2 in range(T):
      list1= []
      for c3 in range(k):
        list1.append(random_list[i])
        i=i+1
      list2.append(list1)
    random_schedule.append(list2)
  return(random_schedule)



def total_goodness(schedule):
  goodness = 0
  for i in range(m):
    for j in range(T):
      goodness = goodness + similarity(schedule[i][j])
  for i in range(T):
    for j1 in range(m):
      for j2 in range((j1+1),m):
        goodness = goodness + C*dissimilarity(schedule[j1][i], schedule[j2][i])
  goodness = round(goodness,3)
  return(goodness)  




def similarity(bucket):
  sum =0
  for i in range(k):
    for j in range((i+1),(k)):
      sum = sum + s[bucket[i]][bucket[j]]
  return(sum)

    

def dissimilarity(bucket1, bucket2):
  sum = 0
  for i in range(k):
    for j in range(k):
      sum = sum + d[bucket1[i]][bucket2[j]]
  return(sum)


def swap_function(schedule_var,j1,j2,l1,l2,i1):
    n1 = []
    n1 = schedule_var
    temp = n1[j1][l1][i1]
    n1[j1][l1][i1] = n1[j2][l2][i1]
    n1[j2][l2][i1] = temp    
    return(n1)




######Main search function########

for count in range(num_restart):
  ############one restart##################
  schedule = random_restart()
  update_flag = 1 #for detecting optima
  local_result_schedule = schedule
  climb = 1
  ##############climb next step##################
  while((update_flag ==1)&(climb<num_climb)): 
    schedule= local_result_schedule
    update_flag = 0   
    climb = climb + 1
    ############successor generate and chose best successor############### 
    local_optimal_goodness = total_goodness(schedule)   
    for i1 in range(k):                           
      for j1 in range(m):
       for j2 in range((j1+1),m):
         for l1 in range(T):
           for l2 in range((l1+1),T):
             neighbor = swap_function(schedule,j1,j2,l1,l2,i1)                          
             if (total_goodness(neighbor)>local_optimal_goodness):
               local_optimal_goodness = total_goodness(neighbor)               
               local_result_schedule = neighbor
               update_flag = 1
    ################# end of successor generate############################
  ################## end of climbing #######################
  

  ##update the result state if a restart gives better goodness##
  if (total_goodness(local_result_schedule)>global_optimal_goodness):
    global_optimal_goodness = total_goodness(local_result_schedule)
    global_result_schedule= local_result_schedule

 ########end of a restart##########


##Adjusting the shop values by adding 1 to it##
for i in range(m):
    for j in range(T):
        if T >= 1:
            global_result_schedule[i][j] = [x + 1 for x in global_result_schedule[i][j]]

## Printing output by separating k shops by space in T time slots by |
## m Parallel shops are divided by a line
for i in range(m):
  for j in range(T):
    if T > 1:
      if j == T-1:
        print(*global_result_schedule[i][j], end=" ")
      else:
        print(*global_result_schedule[i][j], end=" | ")              
    else:
      print(*global_result_schedule[i][j], end="")
  print()
