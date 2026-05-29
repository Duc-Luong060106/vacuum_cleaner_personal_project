from utils import Node, get_solution, compare_state, gen_actions

# Hàm phụ để so sánh trạng thái đã tồn tại trong frontier
def is_state_in_frontier(child_state, frontier):
    for node in frontier:
        if node.state == child_state:
            return True
    
    return False

# cost tính dựa trên g(n), cài đặt bằng số ô còn bụi
def calculate_path_cost(node: Node):
    path_cost = 0 if node.parent == None else node.parent.path_cost

    for i in range(len(node.state)):
        for j in range(len(node.state[0])):
            if node.state[i][j] == 1:
                path_cost += 1
    
    return path_cost

# Lấy ra node có cost bé nhất từ frontier
def pop_lowest_cost_node(frontier):
    lowest_cost_node = min(frontier, key=lambda node: node.path_cost)

    frontier.remove(lowest_cost_node)

    return lowest_cost_node, frontier

# reached là set lưu tuple 2 giá trị state (dạng tuple) và cost
def is_state_in_reached(state, path_cost, reached):
    return (tuple(tuple(row) for row in state), path_cost) in reached
    
    
def uniform_cost_search(initial, goal_test):
    """Thuật toán ucs, cost (h(n)) được tính bằng số ô còn bụi của trạng thái"""
    node = Node(initial, None, None, None)
    node.path_cost = calculate_path_cost(node)

    if compare_state(node.state, goal_test):
        return get_solution(node)

    frontier = []
    frontier.append(node)

    reached = set()

    while frontier:
        node, frontier = pop_lowest_cost_node(frontier)

        reached.add((tuple(tuple(row) for row in node.state), node.path_cost))

        if compare_state(node.state, goal_test):
            return get_solution(node)

        for action, child_state in gen_actions(node.state):

            child = Node(child_state, node, action, None)
            child.path_cost = calculate_path_cost(child)

            if (not is_state_in_frontier(child.state, frontier) and 
                not is_state_in_reached(child.state, child.path_cost, reached)):
                frontier.append(child)

            elif is_state_in_frontier(child.state, frontier):
                child_in_frontier = list(n for n in frontier if n.state == child.state)[0]

                if child.path_cost < child_in_frontier.path_cost:
                    frontier.remove(child_in_frontier)
                    frontier.append(child)

    return None