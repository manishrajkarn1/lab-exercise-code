# defined user_num as u_n.

u_n = int(input("Enter the number:"))
u_n_1 =  int (input("Enter the nubmer:"))
u_n_2 = int (input("Enter the nubmer:"))

# codition to check the largest number.
if u_n > u_n_1 and u_n > u_n_2:
    print(f"The largest number is {u_n} ")
elif u_n_1 > u_n and u_n_1  > u_n_2:
    print(f"The largest number is {u_n_1}")
else:
    print(f"The largest numbe is {u_n_2}")