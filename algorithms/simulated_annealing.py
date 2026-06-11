from utils import Node, get_solution, compare_state, gen_actions

import random
import math

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


def simulated_annealing(initial, goal):
    current_node = Node(initial, None, None, calculate_heuristic_cost(initial))

    T = 100      # Gán cố định
    T_min = 0.01
    alpha = 0.99

    while T > T_min: 
        if compare_state(current_node.state, goal):
            return get_solution(current_node)
        
        action, next_state = random.choice(gen_actions(current_node.state))
        h_cost_next_state = calculate_heuristic_cost(next_state)

        delta = h_cost_next_state - current_node.path_cost
        if delta < 0:
            current_node = Node(next_state, current_node, action, h_cost_next_state)
        else:
            p = math.exp(-delta/T)
            if random.uniform(0, 1) < p:
                current_node = Node(next_state, current_node, action, h_cost_next_state)
        
        T *= alpha

    return None