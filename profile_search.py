from bfs_dfs import (
    START_STATE,
    GOAL_STATE,
    bfs,
    dfs
)


# Run the searches repeatedly so py-spy
# has enough activity to sample.

for _ in range(10000):

    bfs(
        START_STATE,
        GOAL_STATE
    )

    dfs(
        START_STATE,
        GOAL_STATE
    )


print("8-Puzzle profiling completed.")
print("BFS and DFS were executed repeatedly.")