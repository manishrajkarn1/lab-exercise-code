# right traingle star pattern
n = 5

for i in range(1, n + 1):      # outer loop for rows
    for j in range(i):         # inner loop for stars
        print("*", end=" ")
    print()