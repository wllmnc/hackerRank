//https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list
/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position)
{
  // Complete this method only
  // Do not write main function.
    Node* current=head;
    int count=0;
    while(count<position-1 )
    {
        current=current->next;
        count++;
    }
    Node* newNode=(Node*)malloc(sizeof(Node));
    newNode->data=data;
    if(position==0)
    {
        newNode->next=current;        
        head=newNode;        
    }else{
        newNode->next=current->next;
        current->next=newNode;
    }
    return head;
}
