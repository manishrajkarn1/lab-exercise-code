# Write a python program to print the square pattern

n = 5   # size of the square

for i in range(n):          # outer loop for rows
    for j in range(n):      # inner loop for columns
        print("*", end=" ")
    print()