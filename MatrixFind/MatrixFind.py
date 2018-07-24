class MatrixSolution:
    def MatrixFind(self, array, target):
        #检查非空
        if array == []: return False
        row = len(array)
        col = len(array[0])
        print(row)
        print(col)
        #检查输入
        if type(array == float) and type(target) == int:
            array = int(array)
        elif type(array == int) and type(target) == float:
            target = int(target)
        elif type(array) != type(target[0][0]):
            return False

        i = col + 1
        j = 0
        while i >= 0 and j < row:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i == 1
            return True
        #输出数组中目标的个数
def searchMatrix(self, matrix, target):
    if matrix == None or len(matrix) ==0:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    row, col = 0, cols - 1
    count = 0
    while row <= rows - 1 and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            count += 1
            col -= 1
    return count
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80],[63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82],[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83],[66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84],[67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]]

findtarget = MatrixSolution()
print(findtarget.Find(array, 10))
print(findtarget.Find(array, 30))
print(findtarget.Find(array, 13.0))
print(findtarget.Find(array, ''))
print(findtarget.Find(array2, 10))
print(findtarget.Find(array3, 'b'))
print(findtarget.searchMatrix(array4, 81))

findtarget = MatrixSolution()
print(findtarget.Find(array, 10))
print(findtarget.Find(array, 30))
print(findtarget.Find(array, 13.0))
print(findtarget.Find(array, ''))
print(findtarget.Find(array2, 10))
print(findtarget.Find(array3, 'b'))
print(findtarget.searchMatrix(array4, 81))