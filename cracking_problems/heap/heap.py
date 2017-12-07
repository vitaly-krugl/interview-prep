class MinHeap(object):
    """ TODO: generalize for min/max heap
    """
    def __init__(self):
        self.items = []


    def __repr__(self):
        return repr(self.items)


    def insert(self, x):
        # Make room for the new item
        self.items.append(None)

        # Percolate up
        xIdx = len(self.items) - 1
        parentIdx = self._parent(xIdx)
        while xIdx > 0 and x < self.items[parentIdx]:
            self.items[xIdx] = self.items[parentIdx]
            xIdx = parentIdx
            parentIdx = self._parent(xIdx)

        self.items[xIdx] = x


    def removeMin(self):
        """Remove root element and restore the heap

        :return: the root element
        :raise IndexError: if heap is empty
        """
        if not self.items:
            raise IndexError("Heap is empty")


        minValue = self.items[0]

        # Note: this might be the only item, in which case we're done
        lastItem = self.items.pop(-1)

        # Percolate last item down to restore the heap
        if self.items:
            targetIdx = 0
            while True:
                leftChildIdx = self._left(targetIdx)
                rightChildIdx = self._right(targetIdx)

                if rightChildIdx >= len(self.items):
                    # No right child
                    if leftChildIdx >= len(self.items):
                        # No left child either
                        break
                    minChildIdx = leftChildIdx
                else:
                    # Have both children
                    if self.items[leftChildIdx] <= self.items[rightChildIdx]:
                        minChildIdx = leftChildIdx
                    else:
                        minChildIdx = rightChildIdx

                if lastItem > self.items[minChildIdx]:
                    # Move smaller item up a level
                    self.items[targetIdx] = self.items[minChildIdx]
                    targetIdx = minChildIdx
                else:
                    # Subtrees are now in correct position relative to targetIdx
                    break

            self.items[targetIdx] = lastItem

        return minValue


    @staticmethod
    def _parent(i):
        """Given a node index, return its parent node index

        :param i: node's index (0-based)
        :return: the corresponding parent node's index
        """
        return (i - 1) // 2


    @staticmethod
    def _left(i):
        """Given a node's index, return it's left child index

        :param i: node's index (0-based)
        :return: the index of the node's left child
        """
        return i * 2 + 1

    @staticmethod
    def _right(i):
        """Given a node's index, return it's right child index

        :param i: node's index (0-based)
        :return: the index of the node's right child
        """
        return i * 2 + 2