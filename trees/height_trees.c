//https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree?h_r=next-challenge&h_v=zen

/*The tree node has data, left child and right child 
struct node
{
    int data;
    node* left;
    node* right;
};

*/

int sub_getHeight(node * node,int  height_v) 
{
    int height_l=0,height_r=0;
    if(node->left)height_l= sub_getHeight(node->left,height_v+1)+1;
    if(node->right)height_r= sub_getHeight(node->right,height_v+1)+1;
    if(height_l>height_r)
        return height_l;
    else
        return height_r;
}

int height(node * root)
{
  return sub_getHeight(root,0);
}
