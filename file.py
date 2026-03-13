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
"""with open("student.txt",'a') as fp: 
    message = ("there are six studnets present in class.")
    fp.write(message)
print("Writing into file sucess.")"""

# Using exceptional handling to write.

"""try:
    with open("student.txt",'w') as fp:
        message = "We are learning file"
        fp.write("The file chapter has been completed.")
        print("Write sucessfully")
except FileNotFoundError:
    print("oops! File not!")
finally:
    print("exit")"""

#Reading from file:
"""file = open("demo.txt",'w+')
retrive = file.read()
print(retrive)
message = ("HI my name is Manish Raj Karn")
file.write(message)
file.close()"""

# with open("product.txt",'w+') as fp:
#     fp.write("Hello file")
#     print("write into the file sucess")
#     fp.seek(0)
#     reading = fp.read()
#     print(reading)

# file = open("product.txt", 'r+')  # Use 'r+' to read and write without truncating
# retrive = file.read()
# print(retrive)
# file.write("HI my name is Manish raj karn")
# file.close()                    # Added parentheses

"""file = open("product.txt",'w+')
msg = "we are learning seek function."
file.write(msg)
file.seek(0)
reading = file.read()
print(reading)"""

# creating the binary file.

"""file = open("demo.bat",'wb')
print("File created sucessfully")
file.close()"""

# writing on the binary file.

# file = open ("demo.bat",'wb')
# msg = b'Hello world'
# file.write(msg)
# print("write sucessfully")

# reading the binary file.

# file = open("sc600x600.jpg",'rb')
# msg = file.read()
# print(msg)

# writing the file in the numbe of the 

# file = open("number.txt",'w')
# msg = 123456789
# file.write(str(msg))
# file.read(msg)

# print("writign sucessfully")


# file = open("number.txt","r")
# read = int(file.read())
# print(int(read))

# a = type(read)
# print(a)

with open("E:\\python file handling\\file.txt",'w') as fp:
    msg = "file created sucessfully"
    print(msg)
