# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        if not root.left and not root.right: return False
        q = [root, None]
        depth = 0
        dict = {}
        parents = {}
        while q:
            node = q.pop(0)

            if node is None:
                depth += 1
                if q: q.append(None)

            else:
                dict[node.val] = depth

                if node.left:
                    q.append(node.left)
                    parents[node.left.val] = node.val
                if node.right:
                    q.append(node.right)
                    parents[node.right.val] = node.val

        if dict[x] == dict[y] and parents[x] != parents[y]:
            return True
        else:
            return False
        return
