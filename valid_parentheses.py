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
                
