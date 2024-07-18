rows = int(input("\nEnter rows:   "))
columns = int(input("Enter columns:   "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(i*j)
    matrix.append(row)

print("Matrix: ")
for x in matrix:
    print(x)