//https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail
/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head,int positionFromTail)
{
  // This is a "method-only" submission. 
  // You only need to complete this method.
  Node * current=head;
  int lenght=0;
  while(current!=NULL)
  {
      lenght++;
      current=current->next;
  }
  current=head;
  int cont=1;
  while(cont<lenght-positionFromTail)
  {
      cont++;
      current=current->next;
  }
  return current->data;
}
