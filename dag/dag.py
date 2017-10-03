"""
A -> B
A -> C
B -> C
C -> D
C -> E
D -> F
G -> F

isReachable(from, to)

isReachable(A, B) == TRUE
isReachable(A, F) == TRUE
isReachable(B, A) == FALSE
isReachable(A, G) == FALSE
"""


class Node(object):
    def __init__(self):
        self.visited = False
        self.outbound = [] # outbound Nodes
        


def isReachable(frm, to):
    """ Test if "to" Node is reachable from "frm" Node in a DAG
    :param Node frm: (for reviewer: "from" would collide with python keyword)
    :param Node to:
    
    :returns: True if "to" is reachable, False if not
    """
    for node in frm.outbound:
        # Avoid searching a previously-visited sub-DAG
        # ("visited" flags would need to be cleared prior to subsequent search)
        if not node.visited:
            if node is to:
                return True
            else:
                if isReachable(node, to):
                    return True
                    
            node.visited = True
        
    return False

