#creating the file.

"""file = open("demo.txt",'x')
if file: 
    print("file created suscessfully")
else:
    print("File already exxist")"""

#Creating file using with statement.
""""with open("Manish.txt","x") as fp:
    print("File created sucessfully")"""

#Creating using exceptional handling.

"""try:
    file = open("product.txt","x")
    print("File created sucessfully")
    file.close()
except:
    FileNotFoundError
    print("File doesn't exist")"""
# using the with statement in exceptional handling

"""try:
    with open("Student.txt","x") as fp:
        print("File created sucessfully")
except:
    FileNotFoundError
    print("File doesn't exist")"""

#To open write into the file.

"""file = open("demo.txt",'a') # open the file and allow access to write
message = "new data appende?"     # writing the message
writting = file.write(message)      # pirnting the message.
print("Writing into file sucess.")
file.close()"""

# to open the file as with students.
with open("student.txt",'a') as fp: 
    message = ("there are six studnets present in class.")
    fp.write(message)
print("Writing into file sucess.")                                   

