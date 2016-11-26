//https://www.hackerrank.com/challenges/compare-two-linked-lists
/*
  Compare two linked lists A and B
  Return 1 if they are identical and 0 if they are not. 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int CompareLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
    int ans=1;
    Node* currentA=headA;
    Node* currentB=headB;
    while(currentA!=NULL)
    {
        if(currentA->data!=currentB->data)
        {
            ans=0;
            break;
        }
        currentA=currentA->next;
        currentB=currentB->next;
    }
    if(currentB!=NULL)
        ans=0;
    return ans;
}
