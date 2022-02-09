def gcd(num1, num2):
	if num1 == num2:
		return num1
	elif num1>num2:
		return gcd(num1-num2, num2)
	else:
		return gcd(num1, num2-num1)


print(gcd(16, 76))


'''
		m 		m=n
algo (m-n,n)	m>n
	 (m, n-m) 	m<n
'''