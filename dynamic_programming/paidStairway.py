'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''


def paidStairs(cost):
	n = len(cost)
	dp = n*[0]

	dp[0] = cost[0]
	dp[1] = cost[1]

	for i in range(2, n):
		dp[i] = min(dp[i-1], dp[i-2])+cost[i]

	# Since the last step can be taken from either n-2 or n-1
	return min(dp[-1], dp[-2])

cost = [1,100,1,1,1,100,1,1,100,1]
print(paidStairs(cost))