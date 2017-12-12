"""
Topological sort practice problem
"""


class Node(object):
    """A node in the DAG
    """

    def __init__(self, adj):
        """

        :param adj: Sequence of adjacent 0-based node indexes.
        """
        self.adj = tuple(adj)


class DAG(object):
    def __init__(self, nodeSpecs):
        """

        :param nodeSpecs: an ordered sequence of sequences. Each sub-sequence
          represents a node and its elements are 0-based indexes to the adjacent
          nodes relative to the first sub-sequence in this arg. e.g.,
          [
            [3],    # node 0
            [2, 3], # node 1
            [4],    # node 2
            [],     # node 3
            [],     # node 4
          ]

          The graph [[1, 2],[3], [3], [2]] would be an invalid DAG due to the
          cycle [0, 1, 3, 2, 3]

        :raises: ValueError, TypeError if problems found with input args, such
          as non-integer or out-of-range node indexes or cycle in graph.
        """
        self.nodes = []
        for adj in nodeSpecs:
            self.nodes.append(Node(adj))

        # Check for adjacent indexes out of bounds
        for nodeIdx, node in enumerate(self.nodes):
            for adjIdx in node.adj:
                if not isinstance(adjIdx, (int, long)):
                    raise TypeError(
                        "adjIdx {0!r} of node {1} must be int or long".format(
                            adjIdx, nodeIdx))
                if adjIdx < 0 or adjIdx >= len(self.nodes):
                    raise ValueError(
                        "adjIdx {0!r} of node {1} is out of bounds".format(
                            adjIdx, nodeIdx))

        # Check for cycles
        cyclePath = []
        if self.isCyclic(cyclePath=cyclePath):
            raise ValueError("Found cycle in graph: {!r}".format(cyclePath))


    def isCyclic(self, cyclePath=None):
        """

        :param list cyclePath: if a cycle is found, the corresponding node
          indexes will be inserted into this list if it's not None

        :return: True if cycle found in graph, False if not
        """
        if not self.nodes:
            return False

        # Get indexes of nodes without any incoming edges
        rootNodeIndexes = [i for i, count in
                           enumerate(self.getInboundEdgeCounts())
                           if count == 0]
        if not rootNodeIndexes:
            # All nodes have incoming edges, so must be a cycle
            if cyclePath is None:
                return True
            else:
                # Search for cycles from every sub-graph so that we can
                # report a cycle via cyclePath arg
                rootNodeIndexes = list(xrange(len(self.nodes)))


        # Perform (depth first traversal) checking for back edges
        # TODO Should these be inside the for-loop below?
        visited = [False] * len(self.nodes)
        inRecursionStack = [False] * len(self.nodes)

        for rootIdx in rootNodeIndexes:
            if self._isCyclicHelper(rootIdx=rootIdx, visited=visited,
                                    inRecursionStack=inRecursionStack,
                                    cyclePath=cyclePath):
                return True


    def _isCyclicHelper(self, rootIdx, visited, inRecursionStack,
                        cyclePath=None):
        """Use depth-first-traversal to detect if the graph is cyclic.

        :param rootIdx: Index of the sub-graph's root node
        :param visited: list of booleans, each indicating whether the
          sub-graph rooted at the corresponding node has been explored.
        :param inRecursionStack: list of booleans, each indicating whether the
          corresponding node is an ancestor of the node being explored.
        :param list cyclePath: if a cycle is found, the corresponding node
          indexes will be inserted into this list if it's not None

        :return: True if cycle found, False if not
        """
        # The current root is being visited and is in recursion stack
        inRecursionStack[rootIdx] = True

        # Traverse all vertexes adjacent to this one looking for back edges
        # into nodes that are currently in recursion stack.
        for adjIdx in self.nodes[rootIdx].adj:

            if visited[adjIdx]:
                # Sub-graph at adjIdx already explored
                continue

            if inRecursionStack[adjIdx]:
                # Edge from rootIdx to adjIdx is part of a cycle
                if cyclePath is not None:
                    cyclePath.insert(0, adjIdx)
                    cyclePath.insert(0, rootIdx)
                return True

            if self._isCyclicHelper(adjIdx,
                                    visited,
                                    inRecursionStack,
                                    cyclePath):
                if cyclePath is not None:
                    cyclePath.insert(0, rootIdx)
                return True

        # Done exploring the sub-graph rooted at rootIdx
        visited[rootIdx] = True

        # Remove rootIdx node from the exploration path
        inRecursionStack[rootIdx] = False
        return False

    def getTopologicalOrder(self):
        """

        :return: Sequence of the graph's node indexes in topological order
        """
        # Initialize inbound edge counts for all nodes
        inboundEdgeCounts = self.getInboundEdgeCounts()

        # Initialize work queue with indexes of nodes without inbound edges
        workQueue = [i for i, count in enumerate(inboundEdgeCounts)
                     if count == 0]

        # Ordered list will be filled with topologically ordered node indexes
        orderedList = []

        while workQueue:
            # Dequeue the next node index without inbound edges and add it to
            # result
            rootIdx = workQueue.pop(0)
            orderedList.append(rootIdx)

            # Remove root's edges, placing indexes of adjacent nodes that reach
            # 0 inbound count on the work queue
            for adjIdx in self.nodes[rootIdx].adj:
                inboundEdgeCounts[adjIdx] -= 1
                assert inboundEdgeCounts[adjIdx] >= 0
                if inboundEdgeCounts[adjIdx] == 0:
                    workQueue.append(adjIdx)

        if len(orderedList) > len(self.nodes):
            Exception("Logic error - ordered list has more nodes than graph")

        if len(orderedList) < len(self.nodes):
            Exception("Ordered list has fewer nodes than graph = cycle!")

        return orderedList

    def getInboundEdgeCounts(self):
        """

        :return: Sequence of inbound edge counts. Each element in the sequence
          contains the inbound edge counts for the corresponding node in
          self.nodes.
        """
        counts = [0] * len(self.nodes)

        for i, node in enumerate(self.nodes):
            for nodeIdx in node.adj:
                counts[nodeIdx] += 1

        return counts
