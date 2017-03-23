fileName=“testfile.txt”
file = open(fileName,”w”)  
file.write(“Hello World”) 
txt="This is a new text file "
file.write(txt+“ wrote in another line.”) 
file.write(“and this is another extra line.”) 
file.write(“Why? Because we want”)  
file.close() 

file = open(fileName,”r”)  
Lines = file.readlines()
for line in Lines:
  for word in line.split():
    print word,
  print ""
