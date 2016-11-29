//https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle
/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    bool ans=false;
    Node *slow=head;
    Node *fast=NULL;   
    if(slow!=NULL)fast=head->next;   
    while(slow!=NULL && slow->next!=NULL)
    {
        //printf("%x:%x\t",slow->data,fast->data);
        if(slow==fast)
        {
            ans=true;
            break;
        }
        slow=slow->next;
        if(fast->next!=NULL)
            fast=fast->next->next;
    }
    return ans;
}
