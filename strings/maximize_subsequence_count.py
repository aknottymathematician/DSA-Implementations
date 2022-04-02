def maxSubSeqCount(string, patterns):
	count1 = count2 = ans = 0

	for s in string:
		if s == patterns[1]:
			ans+= count1
			count2+=1
		if s == patterns[0]:
			count1+=1

	return max(count1,count2)+ans

print(maxSubSeqCount("abdcdbc", "ac"))