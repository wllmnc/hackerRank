//https://www.hackerrank.com/challenges/binary-search-tree-insertion 
/* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node Insert(Node root,int value)
    {
        if( root!=null)
        if(root.data<value)
        {
            if (root.right!=null)
            {
                Insert(root.right,value);
            }else{
                Node _right=new Node();
                _right.data=value;
                root.right=_right;
            }
        }else{
            if (root.left!=null)
            {
                Insert(root.left,value);
            }else{
                Node _left=new Node();
                _left.data=value;
                root.left=_left;
            }
        }
    else{
        Node _left=new Node();
        _left.data=value;
         root=_left;
    }
        return root;
        
    }


