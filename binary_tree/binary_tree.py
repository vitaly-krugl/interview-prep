"""
Binary tree interview practice
"""


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

    def clear(self):
        self.value = None
        self.left = None
        self.right = None

    def __repr__(self):
        return "%s<%s>" % (self.__class__.__name__, repr(self.value),)


class _NilNode(object):
    """Special marker used by (de)serialization designating a nil child

    """
    pass


class BinaryTree(object):
    """Binary tree; subset of functionality for coding test"""
    
    def __init__(self, initial_values=None):
        """

        :param sequence initial_values: if not None, the values in this sequence
          are used to initialize the tree.
        """
        self._root = None
        if initial_values is not None:
            for value in initial_values:
                self.insert(value)

    def clear(self):
        """Remove all nodes from the tree
        """
        for node in self._postorder_nodes_nr():
            node.clear()

        self._root = None

    def insert(self, value):
        """Insert value into tree
        
        :param value: value to be inserted in tree
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

    def remove(self, key):
        """ Remove a node with value that matches the given key

        :param key: key to match against values in tree
        :return: value of removed node
        :raises: KeyError if matching node not found
        """
        node, parent = self._find_node_and_parent(key)

        value = node.value

        self._remove_node(node, parent)

        return value

    def get_height(self):
        """Get height of the tree non-recursively

        :return: height of the tree
        """
        stack = []
        max_h = 0
        current_h = 0
        node = self._root
        while node is not None or stack:
            while node is not None:
                current_h += 1
                stack.append((node, current_h))
                node = node.left

            max_h = max(max_h, current_h)

            node, current_h = stack.pop()

            # Explore the right subtree
            node = node.right

        return max_h

    def find(self, key):
        """Return a matching value

        :param key: key to match against values in tree
        :return: matching value
        :raises: KeyError if matching node not found
        """
        return self._find_node_and_parent(key)[0].value

    def serialize(self):
        """Serialize

        NOTE: this `serialize()` implementation would also work for a
        non-BST binary tree

        NOTE: not tested yet.

        :return: sequence of values that may be passed to `deserialize()` to
            generate a tree with equal layout of nodes.

        """
        output = []
        self._serialize_subtree(self._root, output)

        return output

    @classmethod
    def _serialize_subtree(cls, node, output):
        """Recursively serializes a tree using pre-order traversal. See
        `serialize()` for more info.

        :param _Node node: Node representing the current subtree to be
            serialized.
        :param list output: List to which serialization output is appended.
            Nodes whose value is None are represented by `_NilNode` class (not
            instance)
        """
        if node is None:
            output.append(_NilNode)
            return

        # Perform a pre-order traversal recursively
        cls._serialize_subtree(node.left, output)
        cls._serialize_subtree(node.right, output)

    @classmethod
    def deserialize(cls, data):
        """Deserializes a tree from the output of `serialize()`

        NOTE: this `deserialize()` implementation would also work for a
        non-BST binary tree

        NOTE: not tested yet.

        :param sequence data: output of `serialize()`
        :return: The binary tree initialized from `serialized_data`.
        """
        tree = BinaryTree()
        tree._root = cls._deserialize_subtree(iter(data))
        return tree

    @classmethod
    def _deserialize_subtree(cls, data_it):
        """Recursively deserialize a subtree from the given serailized data
        iterator.

        :param data_it: iterator of serialized values that may include
            `_NilNode`
        :return: node representing the desrialized subtree
        """
        # NOTE: this should never get StopIteration exception from next because
        # we encode the nil children markers, so recursion ends when those are
        # encountered
        value = next(data_it)
        if issubclass(value, _NilNode):
            return None

        node = _Node(value)
        node.left = cls._deserialize_subtree(data_it)
        node.right = cls._deserialize_subtree(data_it)

        return node

    def matching_values(self, key):
        """ Create a generator that yields matching values

        :param key: the key to match against values in tree
        :return: generator that yields matching values
        :rtype: generator
        """
        # Find the first matching node
        try:
            node = self._find_node_and_parent(key)[0]
        except KeyError:
            node = None

        while node is not None and node.value == key:
            yield node.value

            # Note: our insertion places nodes with equal keys on the left
            node = node.left

    def inorder(self):
        """Generator that yields the tree's values in-order recursively

        Example:
          tree = BinaryTree()
          tree.insert(Node(8))
          tree.insert(Node(-1))
          tree.insert(Node(20))

          for value in tree.inorder():
              print value
        """

        def traverse(node):
            if node is None:
                return

            for value in traverse(node.left):
                yield value

            yield node.value

            for value in traverse(node.right):
                yield value

        return traverse(self._root)

    def inorder_values_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        values in-order

        Example:
          tree = BinaryTree()
          tree.insert(Node(8))
          tree.insert(Node(-1))
          tree.insert(Node(20))

          for value in tree.inorder_values_nr():
              print value
        """
        for node in self._inorder_nodes_nr():
            yield node.value

    def postorder_values_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        values post-order
        """
        for node in self._postorder_nodes_nr():
            yield node.value

    def preorder_values_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        values pre-order
        """
        for node in self._preorder_nodes_nr():
            yield node.value

    def _inorder_nodes_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        nodes in-order
        """
        stack = []
        node = self._root
        while stack or node is not None:
            # Traverse far left, stacking nodes as we go
            while node is not None:
                stack.append(node)
                node = node.left

            # Yield in-order node
            node = stack.pop()
            yield node

            # Traverse the right subtree, if any
            node = node.right

    def _postorder_nodes_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        nodes post-order
        """
        stack = []
        node = self._root
        while stack or node is not None:
            # Traverse far left, stacking nodes as we go
            while node is not None:
                stack.append((node, True))  # set reminder to go right
                node = node.left

            node, goright = stack.pop()

            if goright:
                stack.append((node, False))
                node = node.right
            else:
                yield node
                node = None

    def _preorder_nodes_nr(self):
        """Non-recursive implementation of generator that yields the tree's
        nodes pre-order
        """
        stack = []
        node = self._root
        while stack or node is not None:
            if node:
                yield node
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

    def _find_node_and_parent(self, key):
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

    def _remove_node(self, node, parent):
        """Remove the given node from the tree, taking into account that such
        node could have 0, 1, or two children and adjusting the tree accordingly

        :param Node node: node to remove
        :param Node parent: parent node of the node to remove or None when
          removing the root node.
        :return: None
        """
        if node.left is None or node.right is None:
            # Base case of node having one or zero children: replace parent's
            # link to matching node with the only child or None

            if node.left is not None:
                only_child = node.left
            else:
                only_child = node.right

            if parent is None:
                self._root = only_child
            else:
                if parent.left is node:
                    parent.left = only_child
                else:
                    assert parent.right is node
                    parent.right = only_child
        else:
            # More complicated case of matching node having both children:
            # replace node's value with that of the smallest descendant on its
            # right subtree and remove that descendant
            smallest_right_parent = node
            smallest_right_node = node.right
            while smallest_right_node.left is not None:
                smallest_right_parent = smallest_right_node
                smallest_right_node = smallest_right_node.left

            # Assign the smallest value from the right subtree to the node
            node.value = smallest_right_node.value

            # Recursively delete the smallest node in the right subtree. This
            # should trigger the base case since by definition the smallest node
            # will have no left child and at most one right child.
            assert smallest_right_node.left is None
            self._remove_node(smallest_right_node, smallest_right_parent)
