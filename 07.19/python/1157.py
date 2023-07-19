n = list(input())


lowercase_list = [string.lower() for string in n]


count = {}
for i in lowercase_list:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

max_value = max(list(count.values()))

max_keys = [k for k, l in count.items() if l == max_value]

uppercase_list = [word.upper() for word in max_keys]


if len(max_keys) > 1:
    print('?')
else:
    print(' '.join(uppercase_list))