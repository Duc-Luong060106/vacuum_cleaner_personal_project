from utils import Node, get_solution, compare_state, gen_actions

# Các hàm phụ để so sánh trạng thái đã tồn tại trong frontier và reached hay chưa
def is_state_in_frontier(child_state, frontier):
    for node in frontier:
        if node.state == child_state:
            return True
    
    return False

def is_state_in_reached(child_state, reached):
    return tuple(tuple(row) for row in child_state) in reached


# heuristic cost được tính bằng số ô còn bụi của trạng thái
def calculate_heuristic_cost(node: Node):
    heuristic_cost = 0

    for i in range(len(node.state)):
        for j in range(len(node.state[0])):
            if node.state[i][j] == 1:
                heuristic_cost += 1
    
    return heuristic_cost


def pop_lowest_cost_node(frontier):
    lowest_cost_node = min(frontier, key=lambda node: node.path_cost)

    frontier.remove(lowest_cost_node)

    return lowest_cost_node
    
    
def greedy_search(initial, goal_test):
    node = Node(initial, None, None, None)
    node.path_cost = calculate_heuristic_cost(node)

    if compare_state(node.state, goal_test):
        return get_solution(node)

    frontier = []
    frontier.append(node)

    reached = set()

    while frontier:
        node = pop_lowest_cost_node(frontier)

        reached.add(tuple(tuple(row) for row in node.state))

        if compare_state(node.state, goal_test):
            return get_solution(node)

        for action, child_state in gen_actions(node.state):

            child = Node(child_state, node, action, None)
            child.path_cost = calculate_heuristic_cost(child)

            if (not is_state_in_frontier(child.state, frontier) and 
                not is_state_in_reached(child.state, reached)):
                frontier.append(child)

    return None