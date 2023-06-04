x, y, z, n = 1, 1, 2, 3     #Sample inputs
i, j, k = 0, 0, 0
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])