# https://www.hackerrank.com/challenges/string-validators
s=raw_input()
alphanumeric,alphabetical,digits,lowercase,uppercase=False,False,False,False,False
#In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
for i in xrange(65,91):
    if chr(i) in s:
        uppercase=True
        break
for i in xrange(65,91):
    if chr(i+32) in s:
        lowercase=True
        break
for i in xrange(9):
    if str(i) in s:
        digits=True
        break
alphabetical= uppercase or lowercase
alphanumeric= alphabetical or digits

#In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
print alphanumeric
#In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
print alphabetical
#In the third line, print True if  has any digits. Otherwise, print False. 
print digits
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
print lowercase
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
print uppercase
