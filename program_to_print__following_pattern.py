# Write a python program to print a follwoing pattern using nested loops.

""" * * * * *
    * * * *
    * * *
    * *
    *   """

n = 4   # number of rows

for i in range(n, 0, -1):     # outer loop for rows (decreasing)
    for j in range(i):        # inner loop for printing stars
        print("*", end=" ")
    print()