#This code helps the user to navigate a file

fileName = input("Enter the input file name: ")
filehandle = open(fileName, 'r')
line = filehandle.readline()
while True:
    count = 0
    with open(fileName, 'r') as f:
        for line in f:
            count += 1

    print("Total number of lines is:", count)

    userLine = int(input("Enter a line number [0 to quit]: "))
    if userLine is 0:
        print("You exited the program!!")
        break
    else:
        for i in userLine:
            line = filehandle.readline()
            i += 1
        print(line)

filehandle.close()
