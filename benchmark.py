import timeit

from bfs_dfs import (
    START_STATE,
    GOAL_STATE,
    bfs,
    dfs
)


RUNS = 3
REPETITIONS = 1000


def measure_bfs():

    total_time = timeit.timeit(
        lambda: bfs(
            START_STATE,
            GOAL_STATE
        ),
        number=REPETITIONS
    )

    return (total_time / REPETITIONS) * 1000


def measure_dfs():

    total_time = timeit.timeit(
        lambda: dfs(
            START_STATE,
            GOAL_STATE
        ),
        number=REPETITIONS
    )

    return (total_time / REPETITIONS) * 1000


print("=" * 60)
print("SLE-2: 8-PUZZLE BFS vs DFS PROFILING")
print("=" * 60)

print("Runs:", RUNS)
print("Repetitions per run:", REPETITIONS)
print()

bfs_times = []
dfs_times = []


for run in range(1, RUNS + 1):

    bfs_time = measure_bfs()
    dfs_time = measure_dfs()

    bfs_times.append(bfs_time)
    dfs_times.append(dfs_time)

    print("Run", run)

    print(
        f"BFS Time: {bfs_time:.6f} ms"
    )

    print(
        f"DFS Time: {dfs_time:.6f} ms"
    )

    print()


bfs_average = sum(bfs_times) / RUNS
dfs_average = sum(dfs_times) / RUNS


bfs_found, bfs_nodes = bfs(
    START_STATE,
    GOAL_STATE
)

dfs_found, dfs_nodes = dfs(
    START_STATE,
    GOAL_STATE
)


print("-" * 60)
print("FINAL RESULTS")
print("-" * 60)

print(
    f"BFS Average Time: {bfs_average:.6f} ms"
)

print(
    f"DFS Average Time: {dfs_average:.6f} ms"
)

print(
    "BFS Nodes Expanded:",
    bfs_nodes
)

print(
    "DFS Nodes Expanded:",
    dfs_nodes
)

print(
    "BFS Goal Found:",
    bfs_found
)

print(
    "DFS Goal Found:",
    dfs_found
)