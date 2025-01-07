M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1])     # Row 2
print(M[1][2])      # Row 2, item 3

print([row[1] for row in M])        # Column 2

print([M[row][1] for row in (0, 1, 2)])         # Using offsets

# Diagonals

print([M[i][i] for i in range(len(M))])

print([M[i][len(M) - 1 - i] for i in range(len(M))])

L = [[1, 2, 3], [4, 5, 6]]

for i in range(len(L)):
     for j in range(len(L[i])):         # Update in place
          L[i][j] += 10

print(L)

print([col + 10 for row in M for col in row])          # Assign to M to retain new value

print([[col + 10 for col in row] for row in M])

res = []
for row in M:       # Statement equivalents
     for col in row:          # Indent parts further right
          res.append(col + 10)

print(res)

res = []
for row in M:
     tmp = []       # Left-nesting starts new list
     for col in row:
          tmp.append(col + 10)
     res.append(tmp)

print(res)

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])

print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])


res = []
for row in range(3):
     tmp = []
     for col in range(3):
          tmp.append(M[row][col] * N[row][col])
     res.append(tmp)

print(res)

print([[col1 * col2 for (col1, col2) in zip(row1, row2)]for (row1, row2) in zip(M, N)])