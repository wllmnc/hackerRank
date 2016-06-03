//https://www.hackerrank.com/challenges/tree-level-order-traversal   
/* 
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   void LevelOrder(Node root)
    {
       HashMap<Integer,String> hs=new HashMap<Integer,String>();
       hs.put(0,root.data+" ");
       if(root.left!=null)
       LevelOrder(root.left,hs,1);
       if(root.right!=null)
       LevelOrder(root.right,hs,1);
       
       for(int i=0; i<hs.keySet().size();i++)
            System.out.print(hs.get(i)+"");
    }

    void LevelOrder(Node root, HashMap<Integer,String> hs,int level)
    {
        if (hs.containsKey(level))
            hs.put(level,hs.get(level)+root.data+" ");
        else
            hs.put(level,root.data+" ");
       if(root.left!=null)
            LevelOrder(root.left,hs,level+1);
       if(root.right!=null)
            LevelOrder(root.right,hs,level+1);
    }