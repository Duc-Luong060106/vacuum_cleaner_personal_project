from utils import Node, get_solution, compare_state, gen_actions


# Hàm phụ để so sánh trạng thái đã tồn tại trong frontier
def is_state_in_frontier(child_state, frontier):
    for node in frontier:
        if node.state == child_state:
            return True
    
    return False

def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):
            if state[x][y] == 'X':
                return x, y
            
    return None 


# Chi phí heuristic (h(n)) được tính bằng giá trị nhỏ nhất khoảng cách manhattan từ robot tới bụi
def calculate_heuristic(node: Node):
    x, y = find_vacuum_position(node.state)
    heuristic_cost = 0

    for i in range(len(node.state)):
        for j in range(len(node.state[0])):
            if node.state[i][j] == 1:
                manhattan_distance = abs(x-i) + abs(y-j)
                heuristic_cost = manhattan_distance if heuristic_cost == 0 else min(manhattan_distance, heuristic_cost)
    
    return heuristic_cost

# Chi phí g(n) = g(node cha) + số ô còn bụi của trạng thái
def calculate_g_cost(state):
    g_cost = 0
    for row in state:
        for cell in row:
            if cell == 1:
                g_cost += 1
    return g_cost

# frontier theo kiểu priority queue --> pop phần tử có f(n) nhỏ nhất
def pop_lowest_f_node(frontier):
    lowest_cost_node = min(frontier, key=lambda node: node.path_cost['f'])

    frontier.remove(lowest_cost_node)

    return lowest_cost_node
    
    
def a_star_search(initial, goal_test):
    """Thuật toán A*, g(n) = g(parent) + số ô còn bụi, h(n) bằng khoảng cách manhattan BÉ NHẤT từ robot đến bụi"""
    start = Node(initial, None, None, None)
    g_start = calculate_g_cost(initial)
    h_start = calculate_heuristic(start)
    start.path_cost = {'g': g_start, 'h': h_start, 'f':g_start + h_start}

    if compare_state(start.state, goal_test):
        return get_solution(start)

    frontier = []
    frontier.append(start)

    reached = {}

    while frontier:
        node = pop_lowest_f_node(frontier)
        state_tuple = tuple(tuple(row) for row in node.state)

        reached[state_tuple] = node.path_cost['g']

        if compare_state(node.state, goal_test):
            return get_solution(node)

        for action, child_state in gen_actions(node.state):

            g_new = node.path_cost['g'] + calculate_g_cost(child_state)
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
                h_n = calculate_heuristic(child)
                child.path_cost = {'g': g_n, 'h': h_n, 'f':g_n + h_n}

                frontier.append(child)

    return None