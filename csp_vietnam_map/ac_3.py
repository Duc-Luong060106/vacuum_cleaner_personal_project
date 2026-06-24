from collections import deque
from helper import Csp


def rm_inconsistent_values(xi, xj, domain, csp: Csp):
    removed = False

    for x in domain[xi][::-1]:
        satisfy_constrain = False
        for y in domain[xj]:
            if y != x:
                satisfy_constrain = True
                break

        if not satisfy_constrain:
            domain[xi].remove(x)
            if not domain[xi]:
                return None

            removed = True
    
    return removed

def ac_3(csp: Csp):
    arcs_queue = deque()

    domain = [[cell for cell in row] for row in csp.domain_value]
    for i in range(len(csp.vars)):
        for j in range(len(csp.vars)):
            if csp.constraint[i][j] == 1:
                arcs_queue.append((i, j))

    while arcs_queue:
        xi, xj = arcs_queue.popleft()

        is_rm = rm_inconsistent_values(xi, xj, domain, csp)
        if is_rm == True:
            for x_k in range(len(csp.constraint)):
                if csp.constraint[x_k][xi] == 1:
                    arcs_queue.append((x_k, xi))
        elif is_rm == None:
            return None

    result = dict()
    for i in range(len(csp.vars)):
        result[csp.vars[i]] = tuple(domain[i])

    return result
