//https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list
/*
   Reverse a doubly linked list, input list may also be empty
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* Reverse(Node* head)
{
    // Complete this function
    // Do not write the main method. 
    Node *current=head;    
    if(current!=NULL)
        while(current!=NULL){
        Node *prevTemp=current->prev;
        Node *nextTemp=current->next;
        current->next=prevTemp;
        current->prev=nextTemp;
        if(nextTemp!=NULL)current=nextTemp;
        else break;
        }
    return current;
}
