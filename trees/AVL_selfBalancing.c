/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */
node * insert(node * root, node ** nds,int val);
void   selfBalancing(node * root);
void printTree(node * root);

node * insert(node * root,int val)
{
    //printf("%i\n",val);
    insert(root,&root,val);  
    //printTree(root);
    selfBalancing(root);
    return root;
}
node * insert(node * root, node ** nds,int val )
{
    node ** nextNode;
   if ((*nds)->val>val)
   {
      nextNode=&((*nds)->left);
   }else{
       nextNode=&((*nds)->right);              
   }   
   if(*nextNode!=NULL){
        insert(root,nextNode,val);              
   }else{
        node *temp = NULL;
        temp = (node *)malloc(sizeof(node));
        temp->left = temp->right = NULL;
        temp->val=val;              
        temp->ht=0;
        *nextNode=temp;       
   }
    if((*nds)->ht<(*nextNode)->ht+1)
    {
        (*nds)->ht=(*nextNode)->ht+1;
    }
    return *nextNode;
}

void selfBalancing(node * root)
{
    int BF=0,leftht=0,rightht=0;
    printf("%i",root->val);
    if( root->left !=NULL)
        leftht=root->left->ht+1;
    printf("\tl:%i",leftht);
    if( root->right !=NULL)
        rightht=root->right->ht+1;        
    printf("\tr:%i",rightht);
    BF=leftht-rightht;
    printf("(%i)\n",BF);
    if(!(-1<BF && 1>BF)){               
        if(root->left!=NULL)
            selfBalancing(root->left);
        if(root->right!=NULL)
            selfBalancing(root->right);
    }
    //return root;
}
void printTree(node * root)
{
    printf("%i:%i \n",root->val,root->ht);    
    if(root->left!=NULL)
        printTree(root->left);        
    if(root->right!=NULL)
        printTree(root->right);
}

node* lettRightCase(node * root)
{
	node leftNd=root->left;
	node rightNd=leftNd->right;
	leftNd->right=rightNd->left;
	rightNd->left=leftNd;
	root->left=rightNd;
	return root;
}

node* leftLeftCase(node * root)
{
	node leftNd1=root->left;
	node leftNd2=leftNd1->left;
	root->left=leftNd1->right;
	leftNd1->right=root;
	return leftNd1;
}
node* rightLeftCase(node * root)
{
	node rightNd=root->right;
	node leftNd=rightNd->left;
	rightNd->left=leftNd->right;
	leftNd->right=rightNd;
	root->right=leftNd;
	return root;
}
node* rightRightCase(node * root)
{
	node rightNd1=root->right;
	node rightNd2=rightNd1->right;
	root->right=leftNd1->left;
	rightNd1->left=root;
	return rightNd1;
}
