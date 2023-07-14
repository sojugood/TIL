n = tuple(map(int, input().split()))
y, m, d = n

m_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y2 = y
m2 = m
d2 = d + 1


if d2 > m_days[m - 1]:
    d2 = 1
    m2 = m + 1
    if m2 > 12:
        m2 = 1
        y2 = y + 1

print(f"{m:02d}/{d:02d}/{y}")
print(f"{m2:02d}/{d2:02d}/{y2}")