"""
Binary tree interview practice
"""


class BinaryTree(object):
    """Binary tree; subset of functionality for coding test"""
    
    def __init__(self, initialValues=None):
        """

        :param sequence initialValues: if not None, the values in this sequence
          are used to initialize the tree.
        """
        self._root = None
        if initialValues is not None:
            for value in initialValues:
                self.insert(value)

    def insert(self, value):
        """Insert value into tree
        
        :param node: node to be inserted
        """
        node = _Node(value)

        if self._root is None:
            # Tree was empty
            self._root = node
            return

        # Find where the new node belongs and insert it there
        parent = self._root
        
        while True:
            if value <= parent.value:
                if parent.left is None:
                    parent.left = node
                    break
                else:
                    parent = parent.left
            else:
                if parent.right is None:
                    parent.right = node
                    break
                else:
                    parent = parent.right

    def find(self, key):
        """Return a matching value

        :param key: key to match against values in tree
        :return: matching value
        :raises: KeyError if matching node not found
        """
        return self._findNodeAndParent(key)[0].value

    def matchingValues(self, key):
        """ Create a generator that yields matching values

        :param key: the key to match against values in tree
        :return: generator that yields matching values
        :rtype: generator
        """
        # Find the first matching node
        try:
            node = self._findNodeAndParent(key)[0]
        except KeyError:
            node = None

        while node is not None and node.value == key:
            yield node.value

            # Note: our insertion places nodes with equal keys on the left
            node = node.left

    def remove(self, key):
        """ Remove a node with value that matches the given key

        :param key: key to match against values in tree
        :return: value of removed node
        :raises: KeyError if matching node not found
        """
        node, parent = self._findNodeAndParent(key)

        value = node.value

        self._removeNode(node, parent)

        return value

    def inorder(self):
        """Generator that yields the tree's values in-order

        Example:
          tree = BinaryTree()
          tree.insert(Node(8))
          tree.insert(Node(-1))
          tree.insert(Node(20))

          for value in tree.inorder():
              print value
        """

        def traverse(node):
            """ TODO: rewrite without recursion as cpython has low
            limit on recursion depth.
            """
            if node is None:
                return

            for value in traverse(node.left):
                yield value

            yield node.value

            for value in traverse(node.right):
                yield value

        return traverse(self._root)

    def inorderNR(self):
        """Non-recursive implementation of generator that yields the tree's
        values in-order

        Example:
          tree = BinaryTree()
          tree.insert(Node(8))
          tree.insert(Node(-1))
          tree.insert(Node(20))

          for value in tree.inorderNR():
              print value
        """
        stack = []
        node = self._root
        while stack or node is not None:
            # Traverse far left, stacking nodes as we go
            while node is not None:
                stack.append(node)
                node = node.left

            # Yield in-order value
            node = stack.pop()
            yield node.value

            # Traverse the right subtree, if any
            node = node.right

    def _findNodeAndParent(self, key):
        """Find the first matching node and its parent

        :param key: key to match against values in tree
        :return: two-tuple of matching node and its parent node; the parent will
          be None if the matching node is the root.
        :raises: KeyError if not found
        """
        parent = None
        node = self._root

        while node is not None:
            if node.value == key:
                break

            # Keep looking
            parent = node
            if key <= node.value:
                node = node.left
            else:
                node = node.right
        else:
            raise KeyError

        return node, parent

    def _removeNode(self, node, parent):
        """Remove the given node from the tree, taking into account that such
        node could have 0, 1, or two children and adjusting the tree accordingly

        :param Node node: node to remove
        :param Node parent: parent node of the node to remove or None if the
          former is the root node.
        :return: None
        """

        if node.left is None or node.right is None:
            # Base case of node having one or zero children: replace parent's
            # link to matching node with the the only child or None

            if node.left is None:
                onlyChild = node.right
            else:
                onlyChild = node.left

            if parent is None:
                self._root = onlyChild
            else:
                if parent.left is node:
                    parent.left = onlyChild
                else:
                    assert parent.right is node
                    parent.right = onlyChild
        else:
            # More complicated case of matching node having both children:
            # replace node's value with that of the smallest descendant on its
            # right subtree and remove that descendant
            smallestRightParent = node
            smallestRightNode = node.right
            while smallestRightNode.left is not None:
                smallestRightParent = smallestRightNode
                smallestRightNode = smallestRightNode.left

            # Assign the smallest value from the right subtree to the node
            node.value = smallestRightNode.value

            # Recursively delete the smallest node in the right subtree. This
            # should trigger the base case since by definition the smallest node
            # will have no left children and at most one right child.
            assert smallestRightNode.left is None or \
                   smallestRightNode.right is None
            self._removeNode(smallestRightNode, smallestRightParent)


class _Node(object):
    """Binary tree node for coding test"""

    __slots__ = ("value", "left", "right")

    def __init__(self, value):
        """
        :param value: node's value
        """
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "%s<%s>" % (self.__class__.__name__, repr(self.value),)
