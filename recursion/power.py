def myPow(x, n):
	if n == 0:
		return 1
	else:
		r = myPow(x, n//2)
		if (n%2<0):
			return r*r/x
		elif n%2>0:
			return r*r*x
		else:
			return r*r

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.helper(x, n) #1
        else:
            return 1/self.helper(x, -n) #2
    
    
# Second part
    
    def helper(self, x, n): 
        if n == 0: #3
            return 1
        
        temp = self.myPow(x, n//2) #4
         
        if int(n%2) == 0: #5
            return  temp * temp
        else:
            return temp * temp * x 

sol = Solution()
# print(sol.myPow(0.00001, 2147483647))
print(myPow(2, -2))
    # if(exponent == 0)
    #     return 1;
    # else{
    #     double r = hoch(basis, exponent/2);
    #     if(exponent % 2 < 0)
    #         return r * r / basis;
    #     else if(exponent % 2 > 0)
    #         return r * r * basis;
    #     else
    #         return r * r;