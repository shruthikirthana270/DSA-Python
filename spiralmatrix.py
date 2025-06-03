def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    sr, er = 0, len(matrix) - 1
    sc, ec = 0, len(matrix[0]) - 1
    result = []
    while sr <= er and sc <= ec:
        #left to right
        for i in range(sc, ec + 1):
            result.append(matrix[sr][i])
        sr += 1
        for i in range(sr, er + 1):
            #top to bottom
            result.append(matrix[i][ec])
        ec -= 1
        if sr <= er:
            #right to left
            for i in range(ec, sc - 1, -1):
                result.append(matrix[er][i])
            er -= 1
        if sc <= ec:
            #bottom to top
            for i in range(er, sr - 1, -1):
                result.append(matrix[i][sc])
            sc += 1
    return result

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix row by row:")
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print(spiralOrder(matrix))




