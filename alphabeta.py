import math
import tree


# Actual implementation will depend on how tree and node are implemented
# All node functions are currently placeholders
# INPUTS:
#   node - current node
#   alpha - alpha value
#   beta - beta value
#   isMax - boolean, True if node is a max node, False if node is a min node
def alpha_beta(node, alpha, beta, isMax):
    global leafCount
    # If node is the root, set initial values for alpha and beta
    if node.parent == 0:
        alpha = -math.inf
        beta = math.inf

    # If node is a leaf, just return its value
    if node.leaf:
        leafCount += 1
        return node.value

    print("Node {}: [{}, {}]".format(node.label, alpha, beta))

    # If node is a max node
    if isMax:
        for child in node.children:
            # Get max of alpha and the return of the child node
            alpha = max(alpha, alpha_beta(child, alpha, beta, not isMax))
            print("Node {}: [{}, {}]".format(node.label, alpha, beta))
            if alpha >= beta:
                # Alpha cut - no point in checking the rest
                return beta
        # Alpha is the best value
        return alpha
    # Node is a min node
    else:
        for child in node.children:
            # Get min of beta and the return of the child node
            beta = min(beta, alpha_beta(child, alpha, beta, not isMax))
            print("Node {}: [{}, {}]".format(node.label, alpha, beta))
            if alpha >= beta:
                # Beta cut - no point in checking the rest
                return alpha
    # Beta is the best value
    return beta

def main():
    global leafCount
    tL = tree.readStruct("alphabeta.txt")
    i = 1
    for tr in tL:
        leafCount = 0
        file = open("alphabeta_out.txt","a")
        score = alpha_beta(tr,0,0,True)
        file.write("Graph "+str(i)+": Score: "+str(score)+"; Leaf Nodes Examined: "+str(leafCount)+"\n")
        i += 1
        file.close()
main()
