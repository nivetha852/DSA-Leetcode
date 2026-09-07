class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board =[["."]*n for i in range (n)]
        cols= set()
        dig1=set()
        dig2 = set()
        def backtrack(row):
            if n == row:
                result.append(["".join(r)for r in board])
                return
            for col in range(n):
                if col in cols:
                    continue
                if row-col in dig1:
                    continue
                if row+col in dig2:
                    continue
                board[row][col]="Q"
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                backtrack (row+1)
                board[row][col]="."
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        backtrack(0)
        return result