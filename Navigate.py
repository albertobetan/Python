#This code helps the user to navigate a file
fileName = input("Enter the input file name: ")
filehandle = open(fileName, 'r')
fileList = []
count = 0
with open(fileName, 'r') as f:
    for i in filehandle:
        count += 1
        fileList.append(i)

print("Total number of lines is:", count)
userLine = int(input("Enter a line number [0 to quit]: "))

while userLine != 0:
    if userLine is 0:
        print("You exited the program!!")
    elif userLine > count:
        print("ERROR!!!")
    else:
        print(fileList[userLine - 1])

filehandle.close()
