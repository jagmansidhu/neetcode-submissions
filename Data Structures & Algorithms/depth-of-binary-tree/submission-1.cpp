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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;

        stack<pair<TreeNode*, int>> stack;
        stack.push({root, 1});

        int max = 0;
        while (!stack.empty()) {
            pair<TreeNode*, int> cur = stack.top();
            int data = cur.second;
            stack.pop();

            if (cur.first -> left) stack.push({cur.first -> left, data + 1});
            if (cur.first -> right) stack.push({cur.first -> right, data + 1});
            
            max = std::max(data, max);

        }

        return max;
        
    }
};
