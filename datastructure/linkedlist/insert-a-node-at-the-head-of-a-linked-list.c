//https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list
/*
  Insert Node at the begining of a linked list
  Initially head pointer argument could be NULL for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
return back the pointer to the head of the linked list in the below method.
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
  Node *newNode=(Node*)malloc(sizeof(Node));
  newNode->data=data;
  newNode->next=head;
  return newNode;
}

