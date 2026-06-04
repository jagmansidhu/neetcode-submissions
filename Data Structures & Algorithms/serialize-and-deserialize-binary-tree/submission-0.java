/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {
    final String seperator = ";";
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();;
        q.add(root);
        StringBuilder string = new StringBuilder();

        while (!q.isEmpty()) {
            TreeNode node = q.poll();
        
            if (node == null) {
                string.append("null"+seperator);
                continue;
            }
            
            string.append(node.val).append(seperator);
            
            q.add(node.left);
            q.add(node.right);
        }


        return string.toString();

    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("null;")) return null;

        String[] values = data.split(seperator);
        TreeNode root = new TreeNode(Integer.parseInt(values[0]));
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        int i = 1;
        while (!q.isEmpty() && i < values.length) {
            TreeNode cur = q.poll();

            if (!values[i].equals("null")) {
                TreeNode left = new TreeNode(Integer.parseInt(values[i]));
                cur.left = left;
                q.add(left);
            }

            i++;

            if (!values[i].equals("null")) {
                TreeNode right = new TreeNode(Integer.parseInt(values[i]));
                cur.right = right;
                q.add(right);
            }
            i++;
        }

        return root;
    }
}
