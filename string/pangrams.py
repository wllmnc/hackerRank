#https://www.hackerrank.com/challenges/pangrams
# Enter your code here. Read input from STDIN. Print output to STDOUT
string=raw_input()

def isPangram(str):
    result=True
    for i in range(97,123):
        if not (chr(i) in str or chr(i-32) in str):
            result=False
            break
    return result

print ("not " if not isPangram(string) else "")+"pangram"