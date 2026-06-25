from utils import Node, get_solution, compare_state, gen_actions
import random

def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):

            if state[x][y] == 'X':
                return x, y
    
    return None

# Nhóm thuật toán này sử dụng chi phí heuristic (h(n)), được cài đặt là khoảng cách heuristic XA NHẤT từ robot đến rác.
def calculate_heuristic_cost(state):
    x, y = find_vacuum_position(state)
    heuristic_cost = 0

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 1:
                manhattan_distance = abs(x-i) + abs(y-j)
                heuristic_cost = max(heuristic_cost, manhattan_distance) if heuristic_cost != 0 else manhattan_distance 
    
    return heuristic_cost

def simple_hill_climbing(initial, goal):
    """THuật toán leo đồi đơn giản"""
    current_node = Node(initial, None, None, calculate_heuristic_cost(initial))
    
    while True:
        if compare_state(current_node.state, goal):
            return get_solution(current_node)

        found_better_neighbor = False

        for action, child_state in gen_actions(current_node.state):
            child_cost = calculate_heuristic_cost(child_state)
            if child_cost < current_node.path_cost:
                current_node = Node(child_state, current_node, action, child_cost)
                found_better_neighbor = True
                break
            
        if not found_better_neighbor:
            return None

def steepest_ascent_hill_climbing(initial, goal):
    """Thuật toán leo đồi dốc nhất"""
    current_node = Node(initial, None, None, calculate_heuristic_cost(initial))
    
    while True:
        if compare_state(current_node.state, goal):
            return get_solution(current_node)

        best_neighbor = {"cost": current_node.path_cost-1, "child_info": []}

        for action, child_state in gen_actions(current_node.state):
            child_cost = calculate_heuristic_cost(child_state)

            if child_cost < best_neighbor["cost"]:
                best_neighbor["child_info"] = [(action, child_state)]
                best_neighbor["cost"] = child_cost

            elif child_cost == best_neighbor["cost"]:
                best_neighbor["child_info"].append((action, child_state))
                
        if best_neighbor["child_info"]:
            action, child_state = random.choice(best_neighbor["child_info"])
            current_node = Node(child_state, current_node, action, best_neighbor["cost"])
            
        else:
            return None

def stochastic_hill_climbing(initial, goal):
    """Thuật toán leo đồi ngẫu nhiên"""
    current_node = Node(initial, None, None, calculate_heuristic_cost(initial))
    
    while True:
        if compare_state(current_node.state, goal):
            return get_solution(current_node)

        better_neighbor = []

        for action, child_state in gen_actions(current_node.state):
            child_cost = calculate_heuristic_cost(child_state)

            if child_cost < current_node.path_cost:
                better_neighbor.append((action, child_state, child_cost))
                
        if better_neighbor:
            action, child_state, child_cost = random.choice(better_neighbor)
            current_node = Node(child_state, current_node, action, child_cost)
            
        else:
            return None
        
def random_restart_hill_climbing(initial, goal):
    """Thuật toán leo đồi khởi tạo ngẫu nhiên"""
    MAX_RESTART = 10    # Cài đặt sẵn MAX_RESTART = 10

    for i in range(1, MAX_RESTART + 1):
        current_node = Node(initial, None, None, calculate_heuristic_cost(initial))
    
        while True:
            if compare_state(current_node.state, goal):
                return get_solution(current_node)

            better_neighbor = []

            for action, child_state in gen_actions(current_node.state):
                child_cost = calculate_heuristic_cost(child_state)

                if child_cost < current_node.path_cost:
                    better_neighbor.append((action, child_state, child_cost))
                    
            if better_neighbor:
                action, child_state, child_cost = random.choice(better_neighbor)
                current_node = Node(child_state, current_node, action, child_cost)
                
            else:
                break
    
    return None