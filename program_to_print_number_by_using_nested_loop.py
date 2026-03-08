# Write a  python program to print a follwing pattern using nested loop.

n = 4   # number of rows

for i in range(1, n + 1):      # outer loop for rows
    for j in range(1, i + 1):  # inner loop for numbers
        print(j, end=" ")
    print()