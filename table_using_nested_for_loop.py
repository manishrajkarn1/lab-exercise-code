# write the program to print the table  1 to 20 using the nested loop.

# for i in range(1,11,2):
#     print(i)


for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j}", end=" ")
    print()