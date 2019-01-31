class Solution:
    def isPalindrome_firsttry_recursion(self, x): # 336 ms
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
        
    def isPalindrome_slightly_better_recursion(self, x): # 252 ms
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        x_len = len(x_str)
        if x_len == 1:
            return True
        elif x_len == 2:
            if x_str[0] == x_str[1]:
                return True
            else:
                return False
        elif x_str[0] == x_str[-1]:
            return self.isPalindrome(x_str[1:-1])
        else:
            return False
        
    def isPalindrome_simple(self, x): #256, but beautiful (could be a one liner for +4 ms)
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]
    
    def isPalindrome(self, x, isFirst = True): #248 ms
        """
        :type x: int
        :rtype: bool
        """
        if isFirst: #might speed it up, less use of str conversion
            x_str = str(x)
            x_len = len(x_str)
        else:
            x_str = x
            x_len = len(x)
        if x_len == 1:
            return True
        elif x_len == 2:
            if x_str[0] == x_str[1]:
                return True
            else:
                return False
        elif x_str[0] == x_str[-1]:
            return self.isPalindrome(x_str[1:-1], False) #kinda cheating with optional arg lol
        else:
            return False
