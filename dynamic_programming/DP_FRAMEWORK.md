# FRAMEWORK TO SOLVE DP PROBLEMS
1. Define Objective Function
2. Identify Base Cases
3. Find Recurrence Relation
4. Order of Computation
5. Find Location of Answer
> Note - In most of the cases the answer will be somwhere in **Cache DS**


# Example Stairway Problem
**Question**
> You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

This is a combinatorial problem. To solve the problem the above framework would be used as follows -

1. f(i) - number of distinct ways to reach i<sup>th</sup> stair 
2. f(0) = 1; f(1) = 1
3. f(i) = f(i-1) + f(i-2)$
4. Bottom Up
5. f(n) 
