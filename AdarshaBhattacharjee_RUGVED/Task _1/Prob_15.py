def rotate90(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for row in mat:
        row.reverse()