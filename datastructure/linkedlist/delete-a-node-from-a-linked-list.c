//https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list
/*
  Delete Node at a given position in a linked list 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position)
{
  // Complete this method
    Node* current=head;
    int count=0;
    while(count<position-1)
    {
        count++;
        current=current->next;        
    }
    if(position)
        current->next=current->next->next;
    else
        head=current->next;
    return head;
}
