"""
Binary tree interview practice
"""


class BinaryTree(object):
    """Binary tree; subset of functionality for coding test"""
    
    def __init__(self):
        self._root = None

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

    def find(self, value):
        """Return a matching value

        :param value: value to match
        :return: matching value
        :raises: KeyError if matching node not found
        """
        return self._findNodeAndParent(value)[0].value

    def matchingValues(self, value):
        """ Create a generator that yields matching values

        :param value: the value to match
        :return: generator that yields matching values
        :rtype: generator
        """
        # Find the first matching node
        try:
            node = self._findNodeAndParent(value)[0]
        except KeyError:
            node = None

        while node is not None and node.value == value:
            yield node.value

            # Note: our insertion places nodes with equal keys on the left
            node = node.left

    def remove(self, value):
        """ Remove a node with matching value

        :param value: value to match
        :return: value of removed node
        :raises: KeyError if matching node not found
        """
        node, parent = self._findNodeAndParent(value)

        value = node.value

        self._removeNode(node, parent)

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

    def values(self):
        """Generator that yields the tree's values in-order

        Example:
          tree = BinaryTree()
          tree.insert(Node(8))
          tree.insert(Node(-1))
          tree.insert(Node(20))

          for node in tree.nodes():
              print node
        """

        def traverse(node):
            """ TODO: rewrite without recursion as cpython has low
            limit on recursion depth.
            """
            if node is None:
                return

            for child in traverse(node.left):
                yield child.value

            yield node.value

            for child in traverse(node.right):
                yield child.value

        return traverse(self._root)

    def _findNodeAndParent(self, value):
        """Find the first matching node and its parent

        :param value: value to match
        :return: two-tuple of matching node and its parent node; the parent will
          be None if the matching node is the root.
        :raises: KeyError if not found
        """
        parent = None
        node = self._root

        while node is not None:
            if node.value == value:
                break

            # Keep looking
            parent = node
            if value <= node.value:
                node = node.left
            else:
                node = node.right
        else:
            raise KeyError

        return node, parent


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
