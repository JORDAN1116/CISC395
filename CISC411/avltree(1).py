class AVLTree:

    # AVL tree node
    class Node:
        def __init__(self, element=None):
            self.element = element
            self.left = None
            self.right = None
            self.height = 1

        """return iterable sequence of this node's children"""
        def get_children(self):
            if self.left is not None:
                yield self.left
            if self.right is not None:
                yield self.right

    def __init__(self):
        self.root = None

    """outer wrapper function"""
    def insert(self, key):
        # call inner recursive function
        # start from root
        self.root = self.__insert_helper(key, self.root)
        
    
    """insert key into this tree, inner recursive function"""
    def __insert_helper(self, key, node):
        # perform regular BST insertion
        if node is None:
            return AVLTree.Node(key)
        else:
            if key <= node.element:
                node.left = self.__insert_helper(key, node.left)
            elif key > node.element:
                node.right = self.__insert_helper(key, node.right)
                
        # delect imbalance?
        # update he height of node
        # 1 + max height of its children
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        # calculate balance factor
        balance_factor = self.balance_factor(node)
              
        # determine case
        # detected imbalance
        if balance_factor > 1: # left tree is heavier
            if self.balance_factor(node.left) >= 0: # left tree is heavier
                # LL case
                # before            after
                #       z                y
                #      / \             /   \
                #     y  t0   =>      x     z
                #    / \             / \   / \ 
                #   x  t1           t3 t2 t1 t0
                #  / \ 
                # t3  t2
                # right rotatation on z
                node = self.right_rotate(node)
            else: # right tree is heavier
                # LR case
                # before            after
                #       z                x
                #      / \             /   \
                #     y  t0   =>      y     z
                #    / \             / \   / \ 
                #   t3  x           t3 t2 t1 t0
                #      / \ 
                #    t2  t1    
                # left rotate on node.left
                node.left = self.left_rotate(node.left)
                # right rotate on node
                node = self.right_rotate(node)
        if balance_factor < -1: # right tree is heavier
            if self.balance_factor(node.right) <= 0: # right tree is heavier
                # RR case
                # before            after
                #     z                  y
                #    / \               /   \ 
                #   t0  y       =>    z     x
                #      / \           / \   / \
                #     t1  x         t0 t1 t2 t3
                #         /\
                #       t2 t3
                node = self.left_rotate(node)
            else: # left tree is heavier
                # RL 
                # before            after
                #     z                  x
                #    / \               /   \ 
                #   t0  y       =>    z     y
                #      / \           / \   / \
                #     x  t3         t0 t1 t2 t3
                #    / \
                #   t1 t2
                # right rotate on node.right
                node.right = self.right_rotate(node.right)
                # left rotate on node
                node = self.left_rotate(node)

        # perform rotation to restore balance
        return node

    def left_rotate(self, z):
        #  z          y
        #   \        /
        #    y = >  z
        #   /        \
        #  t2         t2
        y = z.right
        t2 = y.left
        # rotate
        y.left = z
        z.right = t2
        # update
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        #   z           y
        #  /             \
        # y       =>      z
        #  \             /
        #   t2          t2
        y = z.left
        t2 = y.right
        # after
        y.right = z
        z.left = t2
        # update
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y


    def delete(self, key):
        if self.root is None:
            return None
        self.root = self.__delete_helper(key, self.root)

    def __delete_helper(self, key, node):
        if node is None:
            return None
        elif key < node.element:
            # left subtree
            node.left = self.__delete_helper(key, node.left)
        elif key > node.element:
            # right subtree
            node.right = self.__delete_helper(key, node.right)
        else:
            if node.left is None and node.right is None: # no children
                return None
            elif node.left is None: # one child right child
                node = node.right
            elif node.right is None: # one child left child
                node = node.left
            else: # two children
                # get inorder successor
                successor = self.get_successor(node.right)
                # replace its with the successor
                node.element = successor.element
                # delete its inorder successor
                node.right = self.__delete_helper(successor.element, node.right)
        return node

    @staticmethod
    def get_successor(node):
        while node.left is not None:
            node = node.left
        return node 
        
    
    """height difference between left subtree and right subtree"""
    def balance_factor(self, node):
        if node is None:
            return 0
        factor = self.get_height(node.left) - self.get_height(node.right)
        return factor
    
    # utility function
    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return node.height

    
    
if __name__ == '__main__':
    tree = AVLTree()
    
        


    
