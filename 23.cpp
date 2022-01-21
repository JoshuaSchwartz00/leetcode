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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2){
        ListNode* newList = new ListNode();
        ListNode* end = newList;
        ListNode* temp1 = list1;
        ListNode* temp2 = list2;
        
        while(temp1 != nullptr && temp2 != nullptr){
            if(temp1->val >= temp2->val){
                ListNode* newNode = new ListNode(temp2->val);
                end->next = newNode;
                temp2 = temp2->next;
                end = end->next;
            }else if(temp1->val < temp2->val){
                ListNode* newNode = new ListNode(temp1->val);
                end->next = newNode;
                temp1 = temp1->next;
                end = end->next;
            }
        }
        
        if(temp1 == nullptr){
            while(temp2 != nullptr){
                ListNode* newNode = new ListNode(temp2->val);
                end->next = newNode;
                temp2 = temp2->next;
                end = end->next;
            }
        }else if(temp2 == nullptr){
            while(temp1 != nullptr){
                ListNode* newNode = new ListNode(temp1->val);
                end->next = newNode;
                temp1 = temp1->next;
                end = end->next;
            }
        }
        
        return newList->next;
    }
    
    void printList(ListNode* list){
        ListNode* temp = list;
        while(temp != nullptr){
            cout << temp->val << " ";
            temp = temp->next;
        }
        cout << endl;
    }
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()){
            return nullptr;
        }else if(lists.size() == 1){
            return lists[0];
        }
        
        for(int i = lists.size()-1; i >= 0; i--){
            if(lists[i] == nullptr){
                lists.erase(lists.begin()+i);
            }
        }
        
        if(lists.empty()){
            return nullptr;
        }else if(lists.size() == 1){
            return lists[0];
        }
        
        ListNode* answer = new ListNode();
        
        while(lists.size() != 0){
            //mergesort second half
            if(lists.size() == 2){
                answer = mergeTwoLists(lists[0], lists[1]);
                break;
            }else{
                for(int i = (lists.size()/2)-1; i >= 0; i--){
                    ListNode* newList = mergeTwoLists(lists[(2*i)], lists[(2*i)+1]);
                    lists.erase(lists.begin()+(2*i));
                    lists[(2*i)] = newList;
                }
            }
        }
        
        return answer;
    }
};