from numpy import *
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if(len(board) == 0 or len(board[0]) == 0):
        	return bool(0)

        m = len(board)
        n = len(board[0])
        rowFlag = zeros((m, n))
        colFlag = zeros((m , n))
        cellFlag = zeros((m, n))

        for i in range(m):
        	for j in range(n):
        		if(board[i][j] >= '1' and board[i][j] <= '9'):
        			c = int(board[i][j]) - 1
        			if(rowFlag[i][c] or colFlag[c][j] or cellFlag[3 * int(i / 3) + (j / 3)][c]):
        				return bool(0)

        			rowFlag[i][c] = 1
        			colFlag[c][j] = 1
        			cellFlag[3 * int(i / 3) + (j / 3)][c] = 1

        return bool(1)