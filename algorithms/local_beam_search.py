from utils import Node, get_solution, compare_state, gen_actions

import random
import heapq

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

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def local_beam_search(initial, goal, k):
    """Thuật toán local beam search với k trạng thái ban đầu"""
    start = Node(initial, None, None, calculate_heuristic_cost(initial))

    if compare_state(start.state, goal):
        return get_solution(start)
    
    states_from_start = gen_actions(start.state)
    k_start_states = random.sample(states_from_start, min(k, len(states_from_start)))   # Sinh k trạng thái ban đầu

    current_state_set = []

    for action, state in k_start_states:
        node = Node(state, start, action, calculate_heuristic_cost(state))
        if compare_state(node.state, goal):
            return get_solution(node)
        current_state_set.append(node)

    visited = set()     # Tránh lặp vô hạn khi đã duyệt qua tập current đó rồi

    while True:
        current_beam_signature = frozenset(state_to_tuple(node.state) for node in current_state_set)
        if current_beam_signature in visited:
            break       # Nếu bộ k state đó đã xét rồi thì dừng
            
        visited.add(current_beam_signature)
        neighbor_states = dict()

        for node in current_state_set:
            for action, child_state in gen_actions(node.state):

                tuple_state = state_to_tuple(child_state)
                if tuple_state not in neighbor_states:
                    
                    neighbor_states[tuple_state] = Node(child_state, node, action, calculate_heuristic_cost(child_state))

                    if compare_state(child_state, goal):
                        return get_solution(neighbor_states[tuple_state])

        k_best_nodes = heapq.nsmallest(k, neighbor_states.values(), key=lambda node: node.path_cost)
        current_state_set = list(k_best_nodes)

        if not current_state_set:
            return None
    
    return None   