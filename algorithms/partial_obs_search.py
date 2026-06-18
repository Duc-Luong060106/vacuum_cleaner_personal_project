from utils import Node, get_solution, compare_state
import random, copy
from collections import deque

def is_goal(node, goal):
    for state in node.state:
        if not compare_state(state, goal):
            return False
    
    return True

# Các hàm phụ để biến states thành kiểu dữ liệu có thể băm được
def state_set_to_hash(states):
    return frozenset(tuple(tuple(row) for row in state) for state in states)

def is_state_in_reached(states, reached):
    return state_set_to_hash(states) in reached

def is_state_in_frontier(states, frontier):
    state_frozen = state_set_to_hash(states)
    for node in frontier:
        node_frozen = state_set_to_hash(node.state)
        if state_frozen == node_frozen:
            return True
    
    return False

def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):

            if state[x][y] == 'X':
                return x, y
    
    return None

# Tạo ra các trạng thái con hợp lệ và hành động để sinh ra các trạng thái đó
def gen_actions(state):
    m = len(state)
    n = len(state[0])

    x, y = find_vacuum_position(state)

    actions = []

    if x > 0 and state[x-1][y] != 2:
        up_state = [row[:] for row in state]

        up_state[x][y], up_state[x-1][y] = 0, 'X'

        actions.append(("Up", up_state))

    if x < m - 1 and state[x+1][y] != 2:
        down_state = [row[:] for row in state]

        down_state[x][y], down_state[x+1][y] = 0, 'X'

        actions.append(("Down", down_state))

    if y > 0 and state[x][y-1] != 2:
        left_state = [row[:] for row in state]

        left_state[x][y], left_state[x][y-1] = 0, 'X'

        actions.append(("Left", left_state))

    if y < n - 1 and state[x][y+1] != 2:
        right_state = [row[:] for row in state]

        right_state[x][y], right_state[x][y+1] = 0, 'X'

        actions.append(("Right", right_state))

    return actions

# Sinh BS từ môi trường nhìn thấy 1 phần, nhận vào cả S và G (nhưng chỉ có 1 phần)
def generate_belief_state(start, goal):
    valid_positions = []
    
    start_map = copy.deepcopy(start)
    goal_map = copy.deepcopy(goal)
    
    for i in range(len(goal)):
        for j in range(len(goal[0])):
            if start_map[i][j] == 0:
                if goal[i][j] == 2:
                    start_map[i][j] = 2
                    continue
                
                if random.uniform(0, 1) > 0.4:
                    start_map[i][j] = 1
                    valid_positions.append((i, j))
                elif random.uniform(0, 1) < 0.8:
                    start_map[i][j] = 0
                    valid_positions.append((i, j))
                else:
                    start_map[i][j] = 2
                    goal_map[i][j] = 2
            elif start_map[i][j] == 2:
                goal_map[i][j] = 2
    
    belief_state = []
    choosed_bs = random.choices(valid_positions, k=3)
    
    for x, y in choosed_bs:

        new_state = copy.deepcopy(start_map)
        
        new_state[x][y] = 'X'
        
        belief_state.append(new_state)
        
    return belief_state, goal_map   # Tạo BS kèm trạng thái Goal (Khi đã bổ sung thêm vài vật cản)


def partial_obs_search_bfs_version(start, goal_test):
    belief_state, goal_map = generate_belief_state(start, goal_test)
    node = Node(belief_state, None, None, 0)
    
    if is_goal(node, goal_map):
        return get_solution(node)

    frontier = deque()
    frontier.append(node)

    reached = set()

    while frontier:
        node = frontier.popleft()

        reached.add(state_set_to_hash(node.state))

        for move in ["Up", "Down", "Left", "Right"]:
            state_after = []
            for state in node.state:
                new_state = copy.deepcopy(state)
                if compare_state(new_state, goal_map):
                    state_after.append(new_state)
                
                else:
                    can_move = False
                    for action, child_state in gen_actions(state):
                        if action == move:
                            if child_state not in state_after:
                                state_after.append(child_state)
                            can_move = True
                            break
                    
                    if not can_move and new_state not in state_after:
                        state_after.append(new_state)

            child = Node(state_after, node, move, node.path_cost + 1)

            if  not is_state_in_reached(child.state, reached) and not is_state_in_frontier(child.state, frontier):
                
                if is_goal(child, goal_map):
                    return get_solution(child)   
                frontier.append(child)

    return None