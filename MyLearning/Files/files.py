my_file = open('data.txt', 'r')     #r tells that we have opened the file in read mode
file_content = my_file.read() # read takes the entire content of the file and return it as a single string to the variable

my_file.close()    #there is a limit on number of files we can keep open simultaneously so we should always close files which we have worked on
#also we should always close the files at the end of program, we should not left it open
print(file_content)

your_name = input("Enter your name: ")
my_file_writing = open('data.txt', 'w')     #when we open the file in w(writing mode) then the contents of the files gets over written
my_file_writing.write(your_name)

my_file_writing.close()

'''
we can also use the below code for accessing a file contents, the main advantage of the below code is we are not suppose toc lose the with this
syntax as it automatically takes care of it, when we reach the end of the indented block below it automatically closes the file
it is also called context manager
with open('data.txt', 'r') as my_file:
    file_content = my_file.read()
    
'''