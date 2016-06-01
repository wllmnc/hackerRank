/*
   class Node 
       int data;
       Node left;
       Node right;
*/
// https://www.hackerrank.com/challenges/tree-top-view

boolean isLeft=true;
Node childRight;

void top_view(Node root)
{
    top_view(root.left,true);
    System.out.print(root.data+" ");
    top_view(root.right,false);
}

void top_view(Node root, Boolean isLeft)
{
    if (isLeft){
        if(root.left!=null)
        {
            top_view(root.left,true);
        }
        System.out.print(root.data+" ");
    }else{
        System.out.print(root.data+" ");
        if(root.right!=null)
        {
            top_view(root.right,false);
        }
    }
    
}
