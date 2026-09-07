class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows,coloumns = len(matrix),len(matrix[0])
        row ,coloumn = 0,coloumns-1
        while row<rows and coloumn >=0:
            current = matrix[row][coloumn]
            if current == target:
                return True
            elif current> target:
                coloumn = coloumn -1
            else:
                row = row+1
        return False