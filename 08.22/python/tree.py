def preorder(n):
    if n:   # 존재하는 정점이면
        print(n)
        preorder(ch1[n]) # 왼쪽 서브트리로 이동
        preorder(ch2[n]) # 오른쪽 서브트리로 이동


V = int(input()) # 정점 수
E = V - 1 # 간선 수
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식을 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

# 자식을 인덱스로 부모를 저장
par = [0] * (V + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0: # 자식 1이 없으면
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p

print(par)

# 실제 루트 찾기
root = 1
while par[root] != 0:
    root += 1

preorder(root)
