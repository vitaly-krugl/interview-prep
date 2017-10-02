class Node(object):
    """Binary tree node for coding test"""
    
    def __init__(self, value):
        """
        :param value: node's value
        """
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return "%s<%s>" % (self.__class__.__name__, self.value,)


class BinaryTree(object):
    """Binary tree; subset of functionality for coding test"""
    
    def __init__(self):
        self._root = None
        

    def insert(self, value):
        """Insert value into tree
        
        :param value: value to be inserted
        """
        if self._root is None:
            # Tree was empty
            self._root = Node(value)
            return

        # Find where the new value belongs and insert it there
        node = self._root
        
        while True:
            if value <= node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    break
                else:
                    node = node.right


    def values(self):
        """Generator that yields the tree's values in-order
        
        Example:
          tree = BinaryTree()
          tree.insert(8)
          tree.insert(-1)
          tree.insert(20)
          
          for value in tree.values():
              print value
        """
        
        def traverse(tree):
            """ TODO: rewrite without recursion as cpython has low
            limit on recursion depth.
            """
            if tree is None:
                return

            for value in traverse(tree.left):
                yield value

            yield tree.value

            for value in traverse(tree.right):
                yield value
        
        return traverse(self._root)
