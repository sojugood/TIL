import sys
input = sys.stdin.readline

def find_cycle(start, graph):
    visited = [False] * len(graph)
    count = 0
    while True:
        if visited[start]:
            count = 0  # 이미 방문한 노드이므로 사이클이 발생한 것임
            break
        if start == len(graph) - 1:
            break
        visited[start] = True
        count += 1
        start = graph[start] - 1
    return count

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [int(input()) for _ in range(N)]
    print(find_cycle(0, graph))