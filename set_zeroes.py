def set_zeroes(matrix: list[list[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        if i in rows:
            matrix[i] = [0] * n
        for j in range(n):
            if j in cols:
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zeroes(matrix))
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zeroes(matrix))