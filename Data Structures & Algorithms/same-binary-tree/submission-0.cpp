/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;

        queue<pair<TreeNode*, TreeNode*>> queue;
        queue.push({p,q});

        while (!queue.empty()) {
            pair<TreeNode*, TreeNode*> pie = queue.front();
            queue.pop();

            if (!pie.first && !pie.second) continue;
            if (!pie.first || !pie.second || pie.first -> val != pie.second -> val) return false;

            queue.push({pie.first -> left, pie.second -> left});
            queue.push({pie.first -> right, pie.second -> right});

        }

        return true;

        
    }
};
