from collections import deque


# ============================================================
# SLE-2: 8-Puzzle Problem
# BFS vs DFS
# ============================================================

# 0 represents the blank space

START_STATE = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


def get_neighbors(state):
    """Generate all valid next states."""

    neighbors = []

    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero_index], new_state[new_index] = (
                new_state[new_index],
                new_state[zero_index]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def bfs(start, goal):
    """Breadth-First Search for 8-puzzle."""

    queue = deque([start])
    visited = {start}

    nodes_expanded = 0

    while queue:

        current = queue.popleft()

        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded


def dfs(start, goal):
    """Depth-First Search for 8-puzzle."""

    stack = [start]
    visited = {start}

    nodes_expanded = 0

    while stack:

        current = stack.pop()

        nodes_expanded += 1

        if current == goal:
            return True, nodes_expanded

        for neighbor in reversed(get_neighbors(current)):

            if neighbor not in visited:

                visited.add(neighbor)
                stack.append(neighbor)

    return False, nodes_expanded


def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])


if __name__ == "__main__":

    print("=" * 50)
    print("8-PUZZLE: BFS vs DFS")
    print("=" * 50)

    print("\nStart State:")
    print_puzzle(START_STATE)

    print("\nGoal State:")
    print_puzzle(GOAL_STATE)

    bfs_found, bfs_nodes = bfs(
        START_STATE,
        GOAL_STATE
    )

    dfs_found, dfs_nodes = dfs(
        START_STATE,
        GOAL_STATE
    )

    print("\nBFS Results")
    print("-" * 30)
    print("Goal Found:", bfs_found)
    print("Nodes Expanded:", bfs_nodes)

    print("\nDFS Results")
    print("-" * 30)
    print("Goal Found:", dfs_found)
    print("Nodes Expanded:", dfs_nodes)