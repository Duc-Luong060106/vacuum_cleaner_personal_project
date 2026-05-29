from utils import Node, get_solution, compare_state, gen_actions

# Hàm phụ để phát hiện chu trình đối với node hiện tại xét
def is_cycle(node: Node):
    cur = node.parent
    
    while cur != None:
        if cur.state == node.state:
            return True
        
        cur = cur.parent
    
    return False

# Thuật toán Ids cách tiếp cận 1
def iterative_deepening_search_version_1(start, goal):
    """Thuật toán IDS (duyệt theo từng độ sâu) cách tiếp cận 1"""
    max_depth = 100 # Đặt ngưỡng an toàn, tránh cho lặp vô hạn
    for depth in range(0, max_depth+1):
        result = depth_limited_search_version_1(start, goal, depth)

        if result != "cutoff":
            if result == "failure":
                return None
            else: 
                return result
    
    return None


def depth_limited_search_version_1(start, goal, l):
    frontier = [Node(start, None, None, 0)]

    result = "failure"

    while frontier:
        node = frontier.pop()
        
        if compare_state(node.state, goal):
            return get_solution(node)
        
        if node.path_cost >= l:
            result = "cutoff"
        
        elif not is_cycle(node):
            for action, child_state in gen_actions(node.state):
                child = Node(child_state, node, action, node.path_cost + 1)

                frontier.append(child)
        
    return result

# Ids với cách tiếp cận 2
def iterative_deepening_search_version_2(start, goal):
    """Thuật toán IDS (duyệt theo từng độ sâu) cách tiếp cận 2"""
    max_depth = 100
    for depth in range(0, max_depth+1):
        result = depth_limited_search_version_2(start, goal, depth)

        if result != "cutoff":
            if result == "failure":
                return None
            else: 
                return result
    
    return None


def depth_limited_search_version_2(start, goal, l):
    frontier = [Node(start, None, None, 0)]
    
    if compare_state(frontier[-1].state, goal):
        return get_solution(frontier[-1])

    result = "failure"

    while frontier:
        node = frontier.pop()
        
        if node.path_cost >= l:
            result = "cutoff"
        
        elif not is_cycle(node):
            for action, child_state in gen_actions(node.state):
                child = Node(child_state, node, action, node.path_cost + 1)
                
                if compare_state(child.state, goal):
                    return get_solution(child)

                frontier.append(child)
        
    return result