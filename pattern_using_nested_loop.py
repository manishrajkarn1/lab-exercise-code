# Write a python program to print a pattern using nested loops.

n = 5   # number of rows

for i in range(1, n + 1):      # outer loop for rows
    for j in range(1, i + 1):  # inner loop for columns
        print("*", end=" ")
    print()