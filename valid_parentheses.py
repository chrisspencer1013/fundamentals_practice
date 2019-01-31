class Solution:
    def isValid_recursion_firstattempt(self, s): #68ms, 5%
        """
        :type s: str
        :rtype: bool
        """
        #print(s)
        if s == "":
            return True
        elif "()" in s or "{}" in s or "[]" in s:
            return self.isValid(s.replace("()", "").replace("{}", "").replace("[]", ""))
        else:
            return False
                
    def isValid_stack(self, s): #36 ms
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        open_paren = ['(', '{', '[']
        close_paren = [')', '}', ']']
                
        for letter in s:
            if letter in open_paren:
                stack.append(letter)
            elif letter in close_paren:
                if stack == []:
                    return False
                elif open_paren.index(stack.pop()) != close_paren.index(letter): #should be same, otherwise invalid
                    return False
        return True if stack == [] else False
