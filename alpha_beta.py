# Actual implementation will depend on how tree and node are implemented
# All node functions are currently placeholders
# INPUTS:
#   t - tree
#   node - current node
#   alpha - alpha value
#   beta - beta value
#   maxlevel - boolean, True is node is a max node, False if node is a min node
def alpha_beta(t, node, alpha, beta, maxlevel):
    # If node is a leaf, just return its value
    if node.isLeaf():
        return node.getValue()

    print("Node: {}: [{}, {}]".format(node.getName(), alpha, beta))

    # If node is a max node
    if maxlevel:
        for child in node.childNodes:
            # Get max of alpha and the return of the child node
            alpha = max(alpha, alpha_beta(t, child, alpha, beta, not maxlevel))
            print("Node: {}: [{}, {}]".format(node.getName(), alpha, beta))
            if alpha >= beta:
                # Alpha cut
                return beta
        # Alpha is the best value
        return alpha
    # Node is a min node
    else:
        for child in node.childNodes:
            # Get min of beta and the return of the child node
            beta = min(beta, alpha_beta(t, child, alpha, beta, not maxlevel))
            print("Node: {}: [{}, {}]".format(node.getName(), alpha, beta))
            if alpha >= beta:
                # Beta cut
                return alpha
        # Beta is the best value
        return beta