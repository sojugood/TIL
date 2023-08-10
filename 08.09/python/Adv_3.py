def dfs(node, connect_matrix, possible_group, group): # DFS로 두 지역구로 나눌 수 있는 마을의 집합을 생성
    possible_group.add(node) # 각 마을별로 따져봐야 하니까 처음 dfs 시 추가 / 이후 dfs 시에는 연결된 마을이 추가됨
    for i in range(len(connect_matrix)):
        if connect_matrix[node][i] == 1 and i not in possible_group and i in group: # node에 해당하는 마을과 간선으로 연결되어 있고, 지역구에 포함되지 않았으며 부분집합에 포함된 마을일 경우
            dfs(i, connect_matrix, possible_group, group) # 해당 마을에 대하여 탐색
    return possible_group # 모든 탐색 후 지역구에 포함된 마을의 집합 반환

def find_min_diff(connect_matrix, value_list): # 두 지역구 간의 유권자 수 차이의 최소값 계산
    N = len(connect_matrix)
    min_diff = float('inf') # 최소값 찾기 위해 초기값 무한으로 설정
    for i in range(1, 2 ** N - 1): # 가능한 모든 부분집합을 생성(단, 두 지역구로 나뉘어야 하기 때문에 공집합과 전체집합은 제외한다.)
        group_A = [j for j in range(N) if i & (1 << j)] # 가능한 모든 A 지역구 리스트
        group_B = [j for j in range(N) if j not in group_A] # 위 A 지역구에 포함되지 않은 B 지역구의 리스트(1대1 대응)
        if set(group_A) == dfs(group_A[0], connect_matrix, set(), group_A) and set(group_B) == dfs(group_B[0], connect_matrix, set(), group_B): # DFS 탐색을 통해 A 지역구와 B 지역구의 집합 중 연결이 모두 보장되어 있는 경우만을 찾는다.
            diff = abs(sum(value_list[k] for k in group_A) - sum(value_list[k] for k in group_B)) # 각 경우별 유권자 수 차이의 절대값
            min_diff = min(min_diff, diff) # 최소값과 위 경우의 값을 비교하여 최소값을 갱신힌다.
    return min_diff # 최종 최소값 반환

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Rrc = [list(map(int, input().split())) for _ in range(N)]
    Pi = list(map(int, input().split()))
    result = find_min_diff(Rrc, Pi)
    print(f"#{tc} {result}")