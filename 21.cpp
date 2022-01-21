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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr && list2 == nullptr){
            return nullptr;
        }else if(list1 == nullptr){
            return list2;
        }else if(list2 == nullptr){
            return list1;
        }
        
        ListNode* answer = new ListNode();
        ListNode* end = answer;
        
        while(list1 != nullptr && list2 != nullptr){
            if(list1->val >= list2->val){
                ListNode* newNode = new ListNode(list2->val);
                end->next = newNode;
                list2 = list2->next;
                end = end->next;
            }else if(list1->val < list2->val){
                ListNode* newNode = new ListNode(list1->val);
                end->next = newNode;
                list1 = list1->next;
                end = end->next;
            }
        }
        
        if(list1 == nullptr){
            end->next = list2;
        }else if(list2 == nullptr){
            end->next = list1;
        }
        
        return answer->next;
    }
};