//https://www.hackerrank.com/challenges/tree-huffman-decoding
/*  
   class Node
      public  int frequency; // the frequency of this tree
       public  char data;
       public  Node left, right;
    
*/ 

void decode(String S ,Node root)
    {
       int next=0;
       while(next<S.length())
            next=decode(S,next,root);
    }
int decode(String s ,int i,Node root)
{
    if (root.data== '\0')
        if (0==Integer.parseInt(s.charAt(i)+""))
            return decode(s,i+1,root.left);
        else
            return decode(s,i+1,root.right);   
    else
        System.out.print(root.data);
    return i;
}
