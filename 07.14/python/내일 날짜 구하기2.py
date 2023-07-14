from datetime import datetime, timedelta

# 날짜를 입력받는다
y, m, d = map(int, input().split())

# datetime 객체를 생성한다
date = datetime(y, m, d)

# 입력된 날짜를 출력한다
print(date.strftime("%m/%d/%Y"))

# 날짜에 하루를 더한다
next_date = date + timedelta(days=1)

# 다음 날짜를 출력한다
print(next_date.strftime("%m/%d/%Y"))
