class Solution:
    def isPalindrome_bruteforce_recursion(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        #print(x)
        #print(len(x))
        #print(x[1::-1])
        if len(x) == 1:
            return True
        if len(x) == 2:
            if x[0] == x[1]:
                return True
            else:
                return False
        elif x[0] == x[-1]:
            return self.isPalindrome(x[1:-1])
        else:
            return False
