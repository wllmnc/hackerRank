//https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists
/*
   Find merge point of two linked lists
   Node is defined as
   struct Node
   {
       int data;
       Node* next;
   }
*/
int FindMergeNode(Node *headA, Node *headB)
{
    // Complete this function
    // Do not write the main method. 
    Node *currentA=headA;
    Node *currentB=NULL;
    while(currentA!=NULL)
    {
        currentB=headB;
        while (currentB!=NULL)
        {
            if(currentA==currentB)break;
            currentB=currentB->next;
        }
        if(currentB!=NULL)break;        
        currentA=currentA->next;
    }
    return currentA->data;
}
