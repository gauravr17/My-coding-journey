class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # base case: matched every character in word
            if index == len(word):
                return True
            
            # out of bounds, or cell doesn't match, or already used
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False
            
            # temporarily mark this cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # explore all four directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # restore the cell (backtrack)
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False