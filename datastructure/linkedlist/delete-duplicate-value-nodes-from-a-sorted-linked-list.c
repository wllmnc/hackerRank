//https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list
/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head)
{
  // This is a "method-only" submission. 
  // You only need to complete this method. 
    Node *current  =head;
    Node *prevNode =NULL;
    Node *clearNode=NULL;
    int prevValue    =-1;
    while(current!=NULL)
    {
        if(prevValue==current->data){
            clearNode=current;
            prevNode->next=current->next;
            free(clearNode);
        }else{
            prevValue=current->data;
            prevNode=current;
        }        
        current=prevNode->next;
    }
    return head;
}
