'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

#Time Complexity - O(n); Space Complexity - O(n) 
def stairway1(n):
	dp = (n+1)*[None]
	dp[0] = 1
	dp[1] = 1

	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]

	return dp[n]


#Time Complexity - O(n); Space Complexity - O(1)
def stairway2(n):
	a = 1
	b = 1
	for i in range(2, n+1):
		c = a+b
		a = b
		b = c 
	return c


'''
Follow Up Question - What if you can climb k steps at a time? s.t. k<n
'''
Time Complexity - O(nk); Space Complexity - O(n)
def stairwayK1Steps(n, k):
	dp = (n+1)*[0]
	dp[0] = 1
	dp[1] = 1

	for i in range(2, n+1):
		#dp[i] = dp[i-1] + dp[i-2] + dp[i-3]+ ... +dp[i-k] 
		for j in range(1,k+1):
			if i-j<0:
				continue
			dp[i] += dp[i-j]
	return dp[n]

Time Complexity - O(nk); Space Complexity - O(k)
def stairwayK2Steps(n, k):
	dp = (n+1)*[0]
	dp[0] = 1

	for i in range(1, n+1):
		#dp[i] = dp[i-1] + dp[i-2] + dp[i-3]+ ... +dp[i-k] 
		for j in range(1,k):
			if i-j<0:
				continue
			dp[i%k] += dp[(i-j)%k]
	return dp[n%k]


'''
Follow Up Question - What if given n and k, there are also some red steps that you can't climb
'''
def stairwayRedSteps(n, k, red):
	dp = (n+1)*[0]
	dp[0] = 1

	for i in range(1, n+1):
		for j in range(1, k):
			if i-j<0:
				continue
			if stair[i-1]:
				dp[i%k] = 0
			else:
				dp[i%k] += dp[(i-j)%k]
		return dp[n%k]

print(stairwayKSteps(8, 4))
# print(stairway2(8))