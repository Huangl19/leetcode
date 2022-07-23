# 110. 平衡二叉树 简单后续遍历
def isBalanced(root):
    def follow(root):
        if not root:
            return 0

        lh = follow(root.left)
        rh = follow(root.right)
        if lh is False or rh is False or abs(lh - rh) > 1:
            return False
        return max(lh, rh) + 1
    return follow(root) is not False

