"""
To both read from and write to a file, you can use the built-in function  open(), which takes in two parameters: file name and mode. 
File name: the directory path to the file that you want to read or write to. 

Mode: the mode you want to use for the file. The main options are:

Read:  "r"

Write:  "w"

Append:  "a"

Read and write:  "r+" 

To create a new file called “hello.txt” and write “Hello, world!” to it, use the following code:
"""
file = open("test_data.txt", "w")
file.write("Hello, world!")
file.close()

# print each line of a file
with open("test_data.txt") as f:
    for line in f:
        #do something with line
        print(line)