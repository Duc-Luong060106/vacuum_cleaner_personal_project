from helper import Csp

def backtracking_search(csp: Csp):
    return backtrack(csp, {})

def backtrack(csp: Csp, assignment):
    if len(assignment) == len(csp.constraint):
        return assignment
    
    var_idx = len(assignment)

    for value in csp.domain_value[var_idx]:
        is_valid = True
        for assigned_idx in range(var_idx):
            if csp.constraint[var_idx][assigned_idx] == 1 and assignment[csp.vars[assigned_idx]] == value:
                is_valid = False
                break
        if is_valid:
            assignment[csp.vars[var_idx]] = value

            result = backtrack(csp, assignment)
            
            if result is not None:
                return result
            del assignment[csp.vars[var_idx]]
    
    return None