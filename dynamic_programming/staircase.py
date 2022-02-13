'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

#Time Complexity - O(N); Space Complexity - O(N) 
def stairway1(n):
	dp = (n+1)*[None]
	dp[0] = 1
	dp[1] = 1

	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]

	return dp[n]


#Time Complexity - O(N); Space Complexity - O(1)
def stairway2(n):
	a = 1
	b = 1
	for i in range(2, n+1):
		c = a+b
		a = b
		b = c 
	return c

print(stairway2(8))