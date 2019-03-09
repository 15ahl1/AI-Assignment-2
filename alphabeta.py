import math

def alpha_beta(self, node):
    infinity = float('inf')
    best_val = -infinity
    beta = infinity

    successors = self.getSuccessors(node)
    best_state = None
    for state in successors:
        value = self.min_value(state, best_val, beta)
        if value > best_val:
            best_val = value
            best_state = state
    
