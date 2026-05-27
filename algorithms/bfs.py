from collections import deque
from utils import Node, get_solution, compare_state, gen_actions

# Các hàm phụ để so sánh trạng thái đã tồn tại trong frontier và reached hay chưa
def is_state_in_frontier(child_state, frontier):
    for node in frontier:
        if node.state == child_state:
            return True
    
    return False

def is_state_in_reached(child_state, reached):
    return tuple(tuple(row) for row in child_state) in reached

# Bfs với cách tiếp cận 1
def breadth_first_search_version_1(initial, goal_test):
    node = Node(initial, None, None, 0)

    if compare_state(node.state, goal_test):
        return get_solution(node)

    frontier = deque()
    frontier.append(node)

    reached = set()

    while frontier:
        node = frontier.popleft()

        reached.add(tuple(tuple(row) for row in node.state))

        if compare_state(node.state, goal_test):
            return get_solution(node)

        for action, child_state in gen_actions(node.state):

            child = Node(child_state, node, action, node.path_cost + 1)

            if (not is_state_in_frontier(child.state, frontier) and 
                not is_state_in_reached(child.state, reached)):
                frontier.append(child)

    return None

# Bfs với cách tiếp cận 2
def breadth_first_search_version_2(initial, goal_test):
    node = Node(initial, None, None, 0)

    if compare_state(node.state, goal_test):
        return get_solution(node)

    frontier = deque()
    frontier.append(node)

    reached = set()

    while frontier:
        node = frontier.popleft()

        reached.add(tuple(tuple(row) for row in node.state))

        for action, child_state in gen_actions(node.state):

            child = Node(child_state, node, action, node.path_cost + 1)

            if (not is_state_in_frontier(child.state, frontier) and 
                not is_state_in_reached(child.state, reached)):
                
                if compare_state(child.state, goal_test):
                    return get_solution(child)
                
                frontier.append(child)

    return None