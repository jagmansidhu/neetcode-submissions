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
        int count = 0;
        ListNode* temp = head;

        while (temp) {
            temp = temp -> next;
            count ++;
        }

        int remove = count - n;

        if (!remove) return head -> next;

        temp = head;
        for (int i = 0; i < count - 1; i++) {
            if ((i + 1) == remove) {
                temp->next = temp->next->next;
                break;
            }
            temp = temp->next;
        }
        return head;

        
    }
};
