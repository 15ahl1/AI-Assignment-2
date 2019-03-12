import math

# Actual implementation will depend on how tree and node are implemented
# All node functions are currently placeholders
# INPUTS:
#   node - current node
#   alpha - alpha value
#   beta - beta value
#   isMax - boolean, True if node is a max node, False if node is a min node
def alpha_beta(node, alpha, beta, isMax):
    # If node is the root, set initial values for alpha and beta
    if node.isRoot():
        alpha = -math.inf
        beta = math.inf

    # If node is a leaf, just return its value
    if node.isLeaf():
        return node.getValue()

    print("Node {}: [{}, {}]".format(node.getName(), alpha, beta))

    # If node is a max node
    if isMax:
        for child in node.childNodes:
            # Get max of alpha and the return of the child node
            alpha = max(alpha, alpha_beta(child, alpha, beta, not isMax))
            print("Node {}: [{}, {}]".format(node.getName(), alpha, beta))
            if alpha >= beta:
                # Alpha cut - no point in checking the rest
                return beta
        # Alpha is the best value
        return alpha
    # Node is a min node
    else:
        for child in node.childNodes:
            # Get min of beta and the return of the child node
            beta = min(beta, alpha_beta(child, alpha, beta, not isMax))
            print("Node {}: [{}, {}]".format(node.getName(), alpha, beta))
            if alpha >= beta:
                # Beta cut - no point in checking the rest
                return alpha
        # Beta is the best value
        return beta
