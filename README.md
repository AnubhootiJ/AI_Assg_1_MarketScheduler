# AI_Assg_1_MarketScheduler

### Goal:
The goal of this assignment is to take a complex new problem and formulate and solve it as search. Formulation as search is an integral skill of AI that will come in handy whenever you are faced with a new problem. Heuristic search will allow you to find optimal solutions. Local search may not find the optimal solution, but is usually able to find good solutions for really large problems.


### Scenario: Optimization of Market Opening Schedule
A city has n types of shops. The government wants to create an opening schedule for the markets ensuring the safety of maximum people. Due to the current COVID situation the government wants the people to make minimum movement out of their houses. They have approached you to take your help in order to organize the opening of shops in a best possible schedule. You need to use the power of AI and write a generalized search algorithm to find the best possible schedule. 
The city has m market places which can be opened parallely. In a market place during each time slot the government is planning to open k types of shops. And in a day there are a total of T time slots available. We can assume that n = T.m.k. 
For example, in figure below m = 2, T = 3 and k = 4

Type: 1,2,3,4 | Type: 5,6,7,8 | Type: 9,10,11,12
--------------|---------------|-------------------------
Type: 13,14,15,16 | Type: 17,18,19,20 | Type: 21,22,23,24

Now we can define the goodness of a schedule as follows:
Sum(similarities of all pairs within a single time slot in the same market) + C.Sum(distances of all pairs within a single time slot in the parallel market).

The constant C trades off the importance of semantic coherence of one market versus reducing conflict across parallel markets. Your goal is to find a schedule with the maximum goodness.

### Input:
**Line 1**: k: total types of shops opening in one time slot in one market
**Line 2**: m: number of parallel markets
**Line 3**: T: number of time slots
**Line 4**: C: trade-off constant
Starting on the fifth line we have a space separated list of distances between a type of shop and rest others. Note that d(x,y) = d(y,x). Also, all d(x,x) = 0.

### Output Format:
Space separated list of shop ids (i.e, shop’s type ids), where time slots are separated by bars and parallel markets are separated by line.
For the above problem the optimal solution is t1 and t2 in one market; and t3 and t4 in the other market. It will be represented as: 
1 2
3 4
Other equivalent ways to represent this same solution:
4 3
2 1
OR
2 1
3 4
etc. All are valid and have the total goodness of 4.4 

### Approaches used:
1. **Naive Approach**: computing all possible combinations using recursion. Returning schedule with highest goodness score
2. **Hill Climbing with random restarts**: variants were used in the approach like adding time constraint and using tow functions for computing neighbors parallely.
3. **Modified Best first search**: several variants were used with the approach. The final one was performing BFS with selecting a shop initially at random. Also, iterating to create multiple schedules and returning the best one. 
