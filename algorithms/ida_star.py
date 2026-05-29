from utils import Node, get_solution, compare_state, gen_actions

def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):

            if state[x][y] == 'X':
                return x, y
    
    return None

# Hàm phụ để so sánh trạng thái đã tồn tại trong frontier 
def is_state_in_frontier(child_state, frontier):
    for node in frontier:
        if node.state == child_state:
            return True
    
    return False

""" Cách tính các loại chi phí đối với thuật toán này:
    - g(n) = g(parent_node) + cost, với cost tính bằng:
        + Nếu di chuyển vào ô có bụi thì cost = 1
        + Nếu di chuyển vào ô không có bụi thì cost = 3
        Thuật toán sẽ ưu tiên cost bé, tức là ô có bụi.
    - h(n) = khoảng cách manhattan từ robot đến bụi XA NHẤT
    - f(n) = g(n) + h(n)
"""
def calculate_cost(state, action):
    x, y = find_vacuum_position(state)

    match(action):
        case action if action.startswith("Up"):
            return 3 if state[x-1][y] == 0 else 1
        case action if action.startswith("Down"):
            return 3 if state[x+1][y] == 0 else 1
        case action if action.startswith("Left"):
            return 3 if state[x][y-1] == 0 else 1
        case action if action.startswith("Right"):
            return 3 if state[x][y+1] == 0 else 1


def calculate_heuristic_cost(state):
    x, y = find_vacuum_position(state)
    heuristic_cost = 0

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 1:
                manhattan_distance = abs(x-i) + abs(y-j)
                heuristic_cost = max(heuristic_cost, manhattan_distance) if heuristic_cost != 0 else manhattan_distance 
    
    return heuristic_cost

def pop_lowest_cost_node(frontier):
    lowest_cost_node = min(frontier, key=lambda node: node.path_cost['f'])
    frontier.remove(lowest_cost_node)

    return lowest_cost_node


def iterative_deepening_a_star(initial, goal):
    """Thuật toán IDA* với các chi phí:
        - g(n) = g(parent_node) + cost, với cost tính bằng:
            + Nếu di chuyển vào ô có bụi thì cost = 1
            + Nếu di chuyển vào ô không có bụi thì cost = 3
        Thuật toán sẽ ưu tiên cost bé, tức là ô có bụi.
        - h(n) = khoảng cách manhattan từ robot đến bụi XA NHẤT
        - f(n) = g(n) + h(n)
    """
    limit = calculate_heuristic_cost(initial)   # g(n) = 0 --> f(n) = h(n)

    while True:
        result = cost_limited_search(initial, goal, limit)

        if not isinstance(result, tuple):
            if result == "failure":
                return None
            else: 
                return result
        
        limit += result[1]


def cost_limited_search(initial, goal, l):
    start = Node(initial, None, None, None)
    h_start = calculate_heuristic_cost(initial)
    start.path_cost = {'g': 0, 'h': h_start, 'f':h_start}

    if compare_state(start.state, goal):
        return get_solution(start)
    
    frontier = []
    frontier.append(start)

    reached = {}

    result = "failure"
    alpha = None

    while frontier:
        node = pop_lowest_cost_node(frontier)
        
        if compare_state(node.state, goal):
            return get_solution(node)
        
        if node.path_cost['f'] > l:
            alpha = min(node.path_cost['f'], alpha) if alpha != None else node.path_cost['f']
            result = ("cutoff", alpha)
            continue
        
        state_tuple = tuple(tuple(row) for row in node.state)
        reached[state_tuple] = node.path_cost['g']

        for action, child_state in gen_actions(node.state):

            g_new = node.path_cost['g'] + calculate_cost(node.state, action)
            h_n = calculate_heuristic_cost(child_state)
            if g_new + h_n > l:
                alpha = min(g_new + h_n, alpha) if alpha != None else (g_new + h_n)
                result = ("cutoff", alpha)
                continue

            child_state_tup = tuple(tuple(row) for row in child_state)

            if child_state_tup in reached:
                if g_new >= reached[child_state_tup]:
                    continue
                else:
                    del reached[child_state_tup]

            if is_state_in_frontier(child_state, frontier):
                child_in_frontier = list(n for n in frontier if n.state == child_state)[0]
                
                if g_new < child_in_frontier.path_cost['g']:
                    child_in_frontier.parent = node
                    child_in_frontier.path_cost['g'] = g_new
                    child_in_frontier.path_cost['f'] = child_in_frontier.path_cost['g'] + child_in_frontier.path_cost['h']

            elif not is_state_in_frontier(child_state, frontier) and child_state_tup not in reached:
                child = Node(child_state, node, action, None)
                g_n = g_new
                h_n = calculate_heuristic_cost(child_state)
                child.path_cost = {'g': g_n, 'h': h_n, 'f':g_n + h_n}

                frontier.append(child)
        
    return result