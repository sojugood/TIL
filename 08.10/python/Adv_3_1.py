def dfs(node, connect_matrix, possible_group, group):
    possible_group.add(node)
    for i in range(len(connect_matrix)):
        if connect_matrix[node][i] == 1 and i not in possible_group and i in group:
            dfs(i, connect_matrix, possible_group, group)
    return possible_group

def find_min_diff(connect_matrix, value_list):
    N = len(connect_matrix)
    min_diff = float('inf')
    for i in range(1, 2 ** N - 1):
        group_A = [j for j in range(N) if i & (1 << j)]
        group_B = [j for j in range(N) if j not in group_A]
        if set(group_A) == dfs(group_A[0], connect_matrix, set(), group_A) and set(group_B) == dfs(group_B[0], connect_matrix, set(), group_B):
            diff = abs(sum(value_list[k] for k in group_A) - sum(value_list[k] for k in group_B))
            min_diff = min(min_diff, diff)
    return min_diff

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Rrc = [list(map(int, input().split())) for _ in range(N)]
    Pi = list(map(int, input().split()))
    result = find_min_diff(Rrc, Pi)
    print(f"#{tc} {result}")
