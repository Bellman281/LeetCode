class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        int n = 0;
        ListNode* temp = head;
        while(temp) {
            n++;
            temp = temp->next;
        }
        return helper(head,n,k);
    }
    
    ListNode* helper(ListNode*& h, int n, int k) {
        if (n < k || k == 1 || !h) {
            return h;
        }
        ListNode* next = NULL;
        ListNode* new_h = reverse(h,k, next);
        h->next = helper(next, n-k,k);
        return new_h;
    }
    
    ListNode* reverse(ListNode*& h, int k, ListNode*& next) {
        if (k == 1) {
            next = h->next;
            return h;
        }
        
        ListNode* temp = reverse(h->next,--k, next);
        h->next->next = h;
        return temp;
    }
};
