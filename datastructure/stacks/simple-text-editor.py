#https://www.hackerrank.com/challenges/simple-text-editor
n = int(input())
ans = ""
stack_chars= []

for i in range(n):
    myinput = raw_input().strip().split(' ')
    oper=4
    char=""
    if len(myinput)>1:
        oper,char=int(myinput[0]),myinput[1]       
    if oper == 1:
        stack_chars.append(ans)
        ans += char
    elif oper == 2:
        stack_chars.append(ans)
        ans = ans[0:len(ans) - int(char)]
    elif oper == 3:
        print ans[int(char) - 1]
    else:
        ans = stack_chars.pop()
