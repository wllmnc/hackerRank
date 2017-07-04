Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!



wordBreak

a word is breakable iff it consists of one or many legal words from the dictionary

example a, app, apple car
- app le car
- a pple bee
- bedbathandbeyond

counter-example
- c
- applec

input:
string word
... dictionary
output:
boolean

# applebee
# a a a e 

def isBreakable(word, dict):
  count=0
  aCandidates=[]
  s=""
  while count<=len(word): # i = 0 , candidates []
                          # i = 1 , candidates [a]
                          # i = 2 , s=a
                          # i = 3 , s=aa
      s+=word[count]  # ae
      if s in dict:  
        aCandidates.append(s) # candidates [a,a]
        s=""
      temp_string=""
      size=len(aCandidates) # i = 1, len(candidate) = 1
      if s!="":
        for i in range(size)): 
          temp_string+=aCandidates[size-i-1)] # temp_string = a
            if temp_string+s in dict: #aa 
              aCandidates.append(temp_string+s)
                s="" 
      count+=1
  return (s in dict and len(aCandidates)>0) # "" in dict
  
            0      1 2  

aCandidates [a] , 

roxdb 
