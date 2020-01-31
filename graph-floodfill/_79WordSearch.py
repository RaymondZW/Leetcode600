from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or board[0]: return False
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, m, n, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, m, n, i, j, idx):
        if idx >= len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or word[idx] != board[i][j]:
            return False

        # avoid snake eating itself.
        val = board[i][j]
        board[i][j] = '#'
        a = self.dfs(board, word, m, n, i + 1, j, idx + 1)
        b = self.dfs(board, word, m, n, i - 1, j, idx + 1)
        c = self.dfs(board, word, m, n, i, j + 1, idx + 1)
        d = self.dfs(board, word, m, n, i, j - 1, idx + 1)
        board[i][j] = val

        return (a or b or c or d)


sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


sol.exist(board, word)