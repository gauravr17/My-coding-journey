class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        
        result = []
        
        for word in words:
            lower_word = set(word.lower())
            if any(lower_word <= row for row in rows):
                result.append(word)
        
        return result