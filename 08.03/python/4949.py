while True:
    words = input()
    if words == '.':
        break
    test = ''
    for i in words:
        if '[' in i or ']' in i or '(' in i or ')' in i:
            test += i
    if not test:
        print('yes')
    else:
        while True:
            origin = test
            test = test.replace("()", "")
            test = test.replace("[]", "")
            if test == origin:
                print('no')
                break
            elif not test:
                print('yes')
                break
