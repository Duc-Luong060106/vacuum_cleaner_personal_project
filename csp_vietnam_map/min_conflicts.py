import random
from helper import Csp


def is_solution(assignment, csp: Csp):
    for i in range(len(csp.vars)):
        for j in range(i + 1, len(csp.vars)):
            if csp.constraint[i][j] == 1 and assignment[csp.vars[i]] == assignment[csp.vars[j]]:
                return False
    
    return True

def randomly_chosen_conflicted_var(assignment, csp: Csp):
    conflicted_vars = []
    for i in range(len(csp.vars)):
        for j in range(i + 1, len(csp.vars)):
            if csp.constraint[i][j] == 1 and assignment[csp.vars[i]] == assignment[csp.vars[j]]:
                conflicted_vars.extend([csp.vars[i], csp.vars[j]])
    
    return random.choice(conflicted_vars)

def get_value_minimum_conflicts(var, assignment, csp: Csp):
    idx = csp.vars.index(var)

    result = (None, float('inf'))
    for val in csp.domain_value:
        count = 0
        for k in range(len(csp.vars)):
            if csp.constraint[idx][k] == 1 and assignment[csp.vars[k]] == val:
                count += 1
        
        if result[1] > count:
            result = (val, count)
        elif result[1] == count:
            val = random.choice([val, result[0]])
            result = (val, count)
    
    if result[0] != None:
        return result[0]
    return None


def min_conflicts(csp: Csp, max_steps):
    current = dict()
    for i in range(len(csp.vars)):
        current[csp.vars[i]] = random.choice(csp.domain_value)
    
    for i in range(1, max_steps + 1):
        if is_solution(current, csp):
            return current
        var = randomly_chosen_conflicted_var(current, csp)
        value = get_value_minimum_conflicts(var, current, csp)
        if value != None:
            current[var] = value
        
    return None