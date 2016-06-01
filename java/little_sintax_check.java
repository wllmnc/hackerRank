
boolean isCorrectlyNested(String input){
    
    stack st=new st();
    
    for( int i=0;i<input.length();i++)
    {
        char ch=input.charAt(i);
        switch (ch) {
        case "]":
                if st.size()>0) && (st.top()=="[")
                   st.pop();
                else
                    return false;
                break;
        case "}":
                if st.size()>0) && (st.top()=="{")
                   st.pop();
                else
                    return false;
                break;
        case ")":
                if st.size()>0) && (st.top()=="(")
                   st.pop();
                else
                    return false;
                break;
        default:
                st.push(ch); 
        }
    }
    return (st.size()==0);
}

class stack{
    private ArrayList _stack=new ArrayList();
    
    public void push(char item)
    {
        _stack.append(item);
    }
    
    public void pop()
    {
        if(size()>0)
            _stack.remove(size()-1);
    }
    
    public char top()
    {
    	if (size()>0)
        	return _stack[size()-1];
    	else
    		""
    }
    
    public int size()
    {
        return _stack.length();
    }
}
