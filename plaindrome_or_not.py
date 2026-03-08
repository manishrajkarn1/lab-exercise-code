# write the program to check the word is plaindorme or not.
# defined the user_word input as the 'u_w'.

u_w = input("Enter the word, for to check the palindorme or not:")

# condition, by using the slices

if u_w == u_w[::-1]:
    print("This word is the plaindorme.")
else:
    print("This is not plaindorme")

