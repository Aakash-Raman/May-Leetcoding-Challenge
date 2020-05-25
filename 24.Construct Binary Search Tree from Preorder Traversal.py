# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        inorder = sorted(preorder)
        return self.bst(preorder, inorder)
    
    def bst(self, preorder, inorder):
        
        lengthpre = len(preorder)
        lengthin = len(inorder)
        
        if(preorder == None or lengthpre == 0 or lengthpre != lengthin or inorder == None):
            return None
        
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        
        root.left = self.bst(preorder[1:rootindex+1], inorder[:rootindex])
        root.right = self.bst(preorder[rootindex+1:], inorder[rootindex+1:])
        return root
        
        
