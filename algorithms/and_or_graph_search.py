from utils import compare_state
import copy

def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):

            if state[x][y] == 'X':
                return x, y
    
    return None

# Tạo ra các trạng thái con hợp lệ và hành động để sinh ra các trạng thái đó
def generate_actions(state):
    m = len(state)
    n = len(state[0])

    x, y = find_vacuum_position(state)

    actions = []

    if x > 0 and state[x-1][y] != 2:
        actions.append("Up")

    if x < m - 1 and state[x+1][y] != 2:
        actions.append("Down")

    if y > 0 and state[x][y-1] != 2:
        actions.append("Left")

    if y < n - 1 and state[x][y+1] != 2:
        actions.append("Right")

    return actions

# Sinh ra tập các trạng thái sau khi thực hiện hành động
def get_results(state, action):
    m = len(state)
    n = len(state[0])

    move_dict = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    results = []

    x, y = find_vacuum_position(state)
    new_state = copy.deepcopy(state)

    dx, dy = move_dict[action]
    new_state[x][y], new_state[x + dx][y + dy] = 0, "X"

    results.append((action, new_state))
    if x != y:
        return results

    # Các trạng thái lỗi sinh ra tại các ô x = y (VD: (1, 1), (2, 2))
    fault_actions = []
    if action in ["Up", "Down"]:    # Nếu hành động là Up hoặc Down thì nó sinh ra thêm 2 trạng thái lỗi Left và Right
        fault_actions = ["Left", "Right"]
    else:                           # Nếu hành động là Left hoặc Right thì nó sinh ra thêm 2 trạng thái lỗi Up và Down
        fault_actions = ["Up", "Down"]

    for fault_action in fault_actions:
        dx, dy = move_dict[fault_action]
        next_x, next_y = x + dx, y + dy

        if (0 <= next_x < m and 0 <= next_y < n) and state[next_x][next_y] != 2:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[next_x][next_y] = 0, "X"

            results.append((fault_action, new_state))   

    return results     

def state_to_hash(state):
    return tuple(tuple(row) for row in state)

def and_or_graph_search(initial, goal):
    return or_search(initial, goal, [])

def or_search(state, goal, path):
    if compare_state(state, goal):
        return []
    
    if state in path:
        return None
    
    for action in generate_actions(state):
        result_states = get_results(state, action)
        plan = and_search(result_states, goal, path + [state])
        if plan != None:
            return (action, plan)

    return None

def and_search(states, goal, path):
    plans = {}

    for s in states:
        plan_s = or_search(s[1], goal, path)
        if plan_s == None:
            return None
        plans[(s[0], state_to_hash(s[1]))] = plan_s

    return plans