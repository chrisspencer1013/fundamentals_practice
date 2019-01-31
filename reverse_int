class Solution:
    def reverse(self, x): #FASTER THAN 100%!
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            temp =  int(str(x)[::-1])
        else:
            temp =  int("-"+str(abs(x))[::-1])
        
        return 0 if temp < -2**31 or temp > 2**31 else temp
