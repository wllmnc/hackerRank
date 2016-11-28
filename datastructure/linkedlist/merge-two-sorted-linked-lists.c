//https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists
/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
    Node *currentA=headA;
    Node *currentB=headB;
    Node *newHead=(Node*)malloc(sizeof(Node));
    Node *ans=newHead;
    while(currentA!= NULL || currentB!=NULL)
    {          
        
        if(currentA!=NULL && currentB!=NULL)
        {
            if(currentA->data>currentB->data)
            {
                ans->data=currentB->data;
                currentB=currentB->next;
            }else{
                ans->data=currentA->data;
                currentA=currentA->next;
            }
        }else{
            if(currentA!=NULL){
                ans->data=currentA->data;
                currentA=currentA->next;
            }else{
                ans->data=currentB->data;
                currentB=currentB->next;
            }  
        }
        if(currentA!=NULL || currentB!=NULL){
            ans->next=(Node*)malloc(sizeof(Node));
            ans=ans->next;
        }
    }
    return newHead;
}
