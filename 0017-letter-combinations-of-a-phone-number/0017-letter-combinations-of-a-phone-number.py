class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        path = []
        
        def backtrack(index):
            if index == len(digits):
                result.append("".join(path))
                return
            
            letters = digit_to_letters[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1)
                path.pop()  # undo the choice, try the next letter
        
        backtrack(0)
        return result