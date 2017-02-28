"input string only with chars -> ([{}]) "
"output true or fals if there are balanced braces or not into the string"
def validBraces(strBraces):
    openBr,closeBr = "([{",")]}"
    stack = []
    for ch in strBraces:
        if ch in openBr:
            stack.append(ch)
        else:
            if len(stack)>0:
                if stack[len(stack)-1]==openBr[closeBr.find(ch)]:
                    stack.pop()
				else:
					break
            else:
                stack.append(ch)
				break
    return len(stack)==0
