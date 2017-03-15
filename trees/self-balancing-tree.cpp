//https://www.hackerrank.com/challenges/self-balancing-tree
/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

node* leftRightCase(node *);
node* leftLeftCase(node *);
node* rightLeftCase(node *);
node* rightRightCase(node *);
int height(node *);
int max(int , int );
node* newNode(int );
int diff(node *);
node *balance(node *);
node* insert(node *, int );

int height(node *root)
{
    
    int h = -1;
    if (root != NULL)
    {
        int l_height = height (root->left);
        int r_height = height (root->right);
        int max_height = max (l_height, r_height);
        h = max_height + 1;        
        root->ht=h;
    }
    return h;
}
int max(int val1, int val2)
{
    int ans=val1;
    if(val1<val2)
        ans=val2;
    return ans;
}
node* newNode(int val)
{
    node* node_ = (node*)malloc(sizeof(node));
    node_->val    = val;
    node_->left   = NULL;
    node_->right  = NULL;
    node_->ht     = 0;
    return node_;
}
int diff(node *temp)
{
    int l_height = height(temp->left);
    int r_height = height(temp->right);
    int b_factor= l_height - r_height;
    return b_factor;
}
node *balance(node *root)
{
    int bal_factor = diff (root);
    if (bal_factor > 1)
    {
        if (diff (root->left) > 0)
            root = leftLeftCase(root);
        else
            root = leftRightCase(root);
    }
    else if (bal_factor < -1)
    {
        if (diff (root->right) > 0)
            root = rightLeftCase(root);
        else
            root = rightRightCase(root);
    }
    return root;
}
node *insert(node *root, int val)
{  
    if(root==NULL){
        return(newNode(val));
    }
    else{
            if(val<root->val){
                root->left=insert(root->left, val);
            }else if(val>=root->val){
                root->right=insert(root->right, val);
            }
            root = balance(root);
        }
    root->ht=max(height(root->left),height(root->right))+1;
    return root;
}
node* leftRightCase(node *root)
{
	node *leftNd=root->left;
	root->left=rightRightCase(leftNd);
	return leftLeftCase(root);
}

node* rightLeftCase(node *root)
{
	node *rightNd=root->right;
    root->right=leftLeftCase(rightNd);
	return rightRightCase(root);
}
node* leftLeftCase(node *root)
{
    node *new_root;
    new_root = root->left;
    root->left = new_root->right;
    new_root->right = root;
    return new_root;
}
node* rightRightCase(node *root)
{
    node *new_root;
    new_root = root->right;
    root->right = new_root->left;
    new_root->left = root;
    return new_root;
}
