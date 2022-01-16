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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 1;
        ListNode* temp = head;
            
        while(temp->next != nullptr){
            length++;
            temp = temp->next;
        }
        
        if(length <= 1){
            head = nullptr;
        }else if(length == n){
            head = head->next;
        }else{
            int dist = length - n - 1;

            temp = head;
            for(int i = 0; i < dist; i++){
                temp = temp->next;
            }
            
            temp->next = temp->next->next;
        }
        return head;
    }
};