//https://www.hackerrank.com/challenges/reverse-a-linked-list
/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head)
{
  // Complete this method  
    Node* current=head;
    Node* tmpNode=NULL;
    while(current!=NULL)
    {
        Node* copyNode=(Node*)malloc(sizeof(Node));
        copyNode->data=current->data;
        copyNode->next=tmpNode;
        tmpNode=copyNode;
        current=current->next;
    }
    return tmpNode;

}
