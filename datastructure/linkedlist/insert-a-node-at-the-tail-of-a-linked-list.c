//https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list
/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
    Node *headbk=head;
    Node *current=head;
    while(current!=NULL && current->next!=NULL)
    {
        current=current->next;
    }
    Node *newNode=(Node*)malloc(sizeof(Node));
    newNode->data=data;
    newNode->next=NULL;
    if(headbk!=NULL)
        current->next=newNode;
    else
        headbk=newNode;
    return headbk;
    
    
}
