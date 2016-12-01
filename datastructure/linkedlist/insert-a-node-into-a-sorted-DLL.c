//https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list
/*
    Insert Node in a doubly sorted linked list 
    After each insertion, the list should be sorted
   Node is defined as
   struct Node
   {
     int data;
     Node *next;
     Node *prev;
   }
*/
Node* SortedInsert(Node *head,int data)
{
    // Complete this function
   // Do not write the main method. 
    Node *current=head;    
    Node *newNode=(Node*)malloc(sizeof(Node));
    newNode->data=data;
    newNode->next=NULL;
    newNode->prev=NULL;
    
    if(current!=NULL){
        while(current->next!=NULL)            
            if(current->data<data)current=current->next;
            else break;       
        if(current->data>data){
            newNode->next=current;
            newNode->prev=current->prev;
            if(current->prev!=NULL)current->prev->next=newNode;
            else head=newNode;
            current->prev=newNode;
        }else{
            current->next=newNode;
            newNode->prev=current;
             }       
    }else head=newNode;
    return head;
}
