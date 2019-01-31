class Solution:
    def letterCombinations(self, digits): # 32 ms
        """
        :type digits: str
        :rtype: List[str]
        """
        length_digits = len(digits)
        if len(digits) == 0:
            return []
        
        digit_to_letter = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z']
        }
        
        if len(digits) == 1:
            return digit_to_letter[digits]
        

        results = []
        letter_options = []

        for digit in digits:
            letter_options.append(digit_to_letter[digit])

        helper = list(itertools.product(*letter_options))
        
        for letter_list in helper:
            temp = ""
            for letter in letter_list:
                temp += letter
            results.append(temp)
                
        return results
            
