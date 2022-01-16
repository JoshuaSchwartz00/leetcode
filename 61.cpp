/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr){
            return head;
        }
        
        int length = 1;
        ListNode* end = head;
        
        while(end->next != nullptr){
            end = end->next;
            length++;
        }
        
        k = k % length;
        
        ListNode* pivot = head;
        
        for(int i = 0; i < (length-k)-1; i++){
            pivot = pivot->next;
        }
        
        end->next = head;
        head = pivot->next;
        pivot->next = nullptr;
        
        return head;        
    }
};