import timeit

from bfs_dfs import (
    bfs,
    dfs,
    GOAL_STATE
)


# ------------------------------------------------------------
# 8-Puzzle test cases
# ------------------------------------------------------------

CASES = {

    "Best Case": (
        1, 2, 3,
        4, 5, 6,
        7, 0, 8
    ),

    "Average Case": (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    ),

    "Worst Case": (
        1, 6, 2,
        5, 7, 3,
        0, 4, 8
    )
}


RUNS = 3
REPETITIONS = 1000


def benchmark_bfs(start):

    times = []

    for _ in range(RUNS):

        elapsed = timeit.timeit(
            lambda: bfs(
                start,
                GOAL_STATE
            ),
            number=REPETITIONS
        )

        average_ms = (
            elapsed / REPETITIONS
        ) * 1000

        times.append(average_ms)

    return sum(times) / len(times)


def benchmark_dfs(start):

    times = []

    for _ in range(RUNS):

        elapsed = timeit.timeit(
            lambda: dfs(
                start,
                GOAL_STATE
            ),
            number=REPETITIONS
        )

        average_ms = (
            elapsed / REPETITIONS
        ) * 1000

        times.append(average_ms)

    return sum(times) / len(times)


print("=" * 70)
print("SLE-2: 8-PUZZLE BFS vs DFS CASE ANALYSIS")
print("=" * 70)

print("Goal State:")
print(GOAL_STATE)

print()
print("Runs:", RUNS)
print("Repetitions per run:", REPETITIONS)
print()


for case_name, start_state in CASES.items():

    bfs_time = benchmark_bfs(start_state)
    dfs_time = benchmark_dfs(start_state)

    bfs_found, bfs_nodes = bfs(
        start_state,
        GOAL_STATE
    )

    dfs_found, dfs_nodes = dfs(
        start_state,
        GOAL_STATE
    )

    print(case_name)
    print("-" * 70)

    print("Start State:", start_state)

    print(
        f"BFS Average Time: {bfs_time:.6f} ms"
    )

    print(
        "BFS Nodes Expanded:",
        bfs_nodes
    )

    print(
        "BFS Goal Found:",
        bfs_found
    )

    print(
        f"DFS Average Time: {dfs_time:.6f} ms"
    )

    print(
        "DFS Nodes Expanded:",
        dfs_nodes
    )

    print(
        "DFS Goal Found:",
        dfs_found
    )

    print()