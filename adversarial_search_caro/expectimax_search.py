from helper import get_next_turn, generate_next_states, is_terminal, evaluate_if_terminal

class Expectimax:
    def __init__(self, state):
        self.state = state

    def expectimax_search(self):
        turn = get_next_turn(self.state)

        if turn is None:
            return None
        
        if turn == 'X':
            return self.max_value(self.state)
        return self.exp_value(self.state)


    def max_value(self, state):
        if is_terminal(state):
            return evaluate_if_terminal(state), None
        
        best_val, best_pos = float('-inf'), None

        for next_state, pos in generate_next_states(state):
            val, p = self.exp_value(next_state)
            if val > best_val:
                best_val, best_pos = val, pos

        return best_val, best_pos


    def exp_value(self, state):
        if is_terminal(state):
            return evaluate_if_terminal(state), None
        
        children = generate_next_states(state)

        total = 0
        for next_state, pos in children:
            val, p = self.max_value(next_state)
            total += val

        return total / len(children), None