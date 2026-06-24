import copy


def get_next_turn(state):
    '''Kiểm tra trạng thái. 
    Nếu không hợp lệ thì trả về None, nếu hợp lệ trả về lượt tiếp theo X/O'''

    count_x = 0
    count_o = 0

    for row in state:
        for cell in row:
            if cell == 'X':
                count_x += 1
            elif cell == 'O':
                count_o += 1
    
    delta = count_x - count_o
    if abs(delta) > 1:
        return None
    if delta <= 0:
        return 'X'
    return 'O'

# Kiểm tra trạng thái kết thúc và tính điểm: X thắng (1), O thắng (-1), Hòa (0) 
def is_terminal(state):
    def check(a, b, c):
        return (a == b == c) and a != ' '
    
    if (check(state[0][0], state[1][1], state[2][2]) 
        or check(state[0][2], state[1][1], state[2][0])):
        return True
               
    for i in range(3):
        if (check(state[0][i], state[1][i], state[2][i]) 
        or check(state[i][0], state[i][1], state[i][2])):
            return True
    
    for row in state:
        for cell in row:
            if cell == ' ':
                return False
    
    return True


def evaluate_if_terminal(state):
    def check(a, b, c):
        return (a == b == c) and a != ' '
    
    if (check(state[0][0], state[1][1], state[2][2]) 
        or check(state[0][2], state[1][1], state[2][0])):
        return 1 if state[1][1] == 'X' else -1
        
    for i in range(3):
        if check(state[0][i], state[1][i], state[2][i]):
            return 1 if state[0][i] == 'X' else -1
        
        if check(state[i][0], state[i][1], state[i][2]):
            return 1 if state[i][0] == 'X' else -1
    
    return 0        # Dùng evaluate_if_terminal(state) với is_terminal(state) == True, nên loại bỏ các state chưa kết thúc


# Sinh ra các trạng thái tiếp theo (X/O đánh)
def generate_next_states(state):
    fill_char = get_next_turn(state)
    result = [] 

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == ' ':
                new_state = copy.deepcopy(state)
                new_state[i][j] = fill_char
                result.append((new_state, (i, j)))

    return result
