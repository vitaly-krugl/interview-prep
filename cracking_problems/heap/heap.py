class MinHeap(object):
    """ TODO: generalize for min/max heap
    """
    def __init__(self):
        # Reserve 0th element for algorithmic convenience
        self.items = [None]


    def __repr__(self):
        return repr(self.items)


    def insert(self, x):
        xPos = len(self.items)

        # Make room for the new item
        self.items.append(None)

        # Percolate up
        while xPos > 1 and x < self.items[xPos // 2]:
            self.items[xPos] = self.items[xPos // 2]
            xPos //= 2

        self.items[xPos] = x


    def deleteMin(self):
        """Remove root element and restore the heap

        :return: the root element
        """
        if len(self.items) <= 1:
            raise IndexError("Heap is empty")


        x = self.items[1]

        lastItem = self.items.pop(-1)

        if len(self.items) > 1:
            # Percolate last item down to restore the heap
            targetIdx = 1
            while True:
                leftChildIdx = targetIdx * 2
                rightChildIdx = targetIdx * 2 + 1

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
                    # Swap
                    self.items[targetIdx] = self.items[minChildIdx]
                    targetIdx = minChildIdx
                else:
                    break

            self.items[targetIdx] = lastItem

        return x
