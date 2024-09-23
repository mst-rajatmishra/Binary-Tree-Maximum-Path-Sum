class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')  # Initialize global maximum sum
        
        def max_gain(node):
            if not node:
                return 0
            
            # Compute the maximum gain from left and right subtrees
            left_gain = max(max_gain(node.left), 0)  # Only consider positive gains
            right_gain = max(max_gain(node.right), 0)
            
            # Calculate the price of the current node being the highest point
            price_newpath = node.val + left_gain + right_gain
            
            # Update the global maximum sum
            self.max_sum = max(self.max_sum, price_newpath)
            
            # Return the maximum gain from the current node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)  # Start the recursion
        return self.max_sum

