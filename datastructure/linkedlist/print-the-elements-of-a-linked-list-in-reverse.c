//https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse
/*
  Print elements of a linked list in reverse order as standard output
  head pointer could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
void ReversePrint(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method. 
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
    while(tmpNode!=NULL)
    {
        printf("%d\n",tmpNode->data);
        tmpNode=tmpNode->next;
    }
}
