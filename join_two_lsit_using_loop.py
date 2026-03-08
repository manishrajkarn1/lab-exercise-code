list1 = [1,2,3,4,5]
list2 = [2,6,4,7,8]
fileter_list = []
list3 = list1 + list2
# for newlist in list1:
#     list2.append(newlist)

for item in list3:
    if item not in fileter_list:
        fileter_list.append(item)
print(fileter_list)
