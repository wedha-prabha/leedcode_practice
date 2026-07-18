class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        # Map digits to their corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # If the current combination is done
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                path.append(letter)      # Move forward
                backtrack(index + 1, path) # Recurse next digit
                path.pop()               # Backtrack
                
        backtrack(0, [])
        return res