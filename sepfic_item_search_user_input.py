list1 = [1, 2, 3, 4, 5, 6]
search = int(input("Enter the value to search: "))

found = False

for item in list1:
    if item == search:
        print(f"{item} item is found")
        found = True
        break

else:
    print(f"{search} item is not found")