#file operation 

#read file
f = open('inputFile.txt','r')
passFile = open('PassFile.txt','w')# helps to creatre a new File
failFile= open('failFile.txt','w') # file for fails
count = 0
for  line in f: # for loop in python
    line_split = line.split() #splits the test string into array
    if line_split[2] =='P':
        # print(line)
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()