import copy
from helper import Csp


def forward_checking_search(csp: Csp):
    return forward_check(csp, {})

def forward_check(csp: Csp, assignment):
    if len(assignment) == len(csp.domain_value):
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

            remain_domain_value = copy.deepcopy(csp.domain_value)
            is_valid_forward = True

            for unassigned in range(var_idx + 1, len(csp.vars)):
                if csp.constraint[unassigned][var_idx] == 1 and value in csp.domain_value[unassigned]:
                    csp.domain_value[unassigned].remove(value)
                    if not csp.domain_value[unassigned]:
                        csp.domain_value = remain_domain_value
                        is_valid_forward = False
                        break
            
            if is_valid_forward:
                result = forward_check(csp, assignment)
                
                if result is not None:
                    return result
                
            del assignment[csp.vars[var_idx]]
            csp.domain_value = remain_domain_value
    
    return None