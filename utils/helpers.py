from .node import Node


def get_solution(node):
    path = []

    while node != None:
        path.append(node)
        node = node.parent

    path.reverse()
    return path


# So sánh trạng thái với trạng thái đích (Không còn bụi)
def compare_state(state, goal_state):
    for x in range(len(state)):
        for y in range(len(state[0])):
            # Vị trí của robot đang đứng xem như đã hút sạch bụi
            if state[x][y] != 'X' and state[x][y] != goal_state[x][y]:
                return False

    return True


def find_vacuum_position(state):
    for x in range(len(state)):
        for y in range(len(state[0])):

            if state[x][y] == 'X':
                return x, y
    
    return None


# Tạo ra các trạng thái con
def gen_actions(state):
    m = len(state)
    n = len(state[0])

    x, y = find_vacuum_position(state)

    actions = []

    if x > 0 and state[x-1][y] != 2:
        up_state = [row[:] for row in state]
        clean_action = f" và dọn rác ô [{x-1}][{y}]" if up_state[x-1][y] == 1 else ""

        up_state[x][y], up_state[x-1][y] = 0, 'X'

        actions.append(("Up" + clean_action, up_state))

    if x < m - 1 and state[x+1][y] != 2:
        down_state = [row[:] for row in state]
        clean_action = f" và dọn rác ô [{x+1}][{y}]" if down_state[x+1][y] == 1 else ""

        down_state[x][y], down_state[x+1][y] = 0, 'X'

        actions.append(("Down" + clean_action, down_state))

    if y > 0 and state[x][y-1] != 2:
        left_state = [row[:] for row in state]
        clean_action = f" và dọn rác ô [{x}][{y-1}]" if left_state[x][y-1] == 1 else ""

        left_state[x][y], left_state[x][y-1] = 0, 'X'

        actions.append(("Left" + clean_action, left_state))

    if y < n - 1 and state[x][y+1] != 2:
        right_state = [row[:] for row in state]
        clean_action = f" và dọn rác ô [{x}][{y+1}]" if right_state[x][y+1] == 1 else ""

        right_state[x][y], right_state[x][y+1] = 0, 'X'

        actions.append(("Right" + clean_action, right_state))

    return actions