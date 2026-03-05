rows = int(input("Enter row size: "))
cols = int(input("Enter column size: "))

L = []

# Input matrix
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("Enter value: "))
        row.append(val)
    L.append(row)

# Print matrix
print("Matrix:")
for i in range(rows):
    for j in range(cols):
        print(L[i][j], end=" ")
    print()

# Row sums
print("\nROW SUMS")
for i in range(rows):
    s = 0
    for j in range(cols):
        s += L[i][j]
    print("Sum of row", i, "=", s)

# Column sums
print("\nCOLUMN SUMS")
for j in range(cols):
    s = 0
    for i in range(rows):
        s += L[i][j]
    print("Sum of column", j, "=", s)

# Diagonal sums (only for square matrix)
if rows == cols:
    left_diag = 0
    right_diag = 0

    for i in range(rows):
        left_diag += L[i][i]
        right_diag += L[i][rows - 1 - i]

    print("\nDiagonal Sums")
    print("Left diagonal =", left_diag)
    print("Right diagonal =", right_diag)
else:
    print("\nDiagonal sums only possible for square matrix")