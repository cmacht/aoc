with open("input") as f:
    # inst = [lvl.split() for lvl in f.read().splitlines()]
    inst = f.read()

print(inst)

cur = None
temp = None
fac1 = 0
fac2 = 0
ans = 0

xcur = None
enabled = True


for c in inst:

    if xcur is None and c == 'd':
        xcur = 'd'
    elif xcur == 'd' and c == 'o':
        xcur = 'do'
    elif xcur == 'do' and c == '(':
        xcur = 'do('
    elif xcur == 'do(' and c == ')':
        enabled = True
        xcur = None
    elif xcur == 'do' and c == 'n':
        xcur = 'don'
    elif xcur == 'don' and c == '\'':
        xcur = 'don\''
    elif xcur == 'don\'' and c == 't':
        xcur = 'don\'t'
    elif xcur == 'don\'t' and c == '(':
        xcur = 'don\'t('
    elif xcur == 'don\'t(' and c == ')':
        enabled = False
        xcur = None
    else:
        xcur = None


    if cur is None and c == 'm':
        cur = 'm'
    elif cur == 'm' and c == 'u':
        cur = 'mu'
    elif cur == 'mu' and c == 'l':
        cur = 'mul'
    elif cur == 'mul' and c == '(':
        cur = 'mul('
    elif cur == 'mul(' and temp is None and c.isdigit():
        temp = c
    elif cur == 'mul(' and temp is not None and c.isdigit():
        temp += c
    elif cur == 'mul(' and temp is not None and c == ',':
        cur = 'mul(,'
        fac1 = int(temp)
        temp = None
    elif cur == 'mul(,' and temp is None and c.isdigit():
        temp = c
    elif cur == 'mul(,' and temp is not None and c.isdigit():
        temp += c
    elif cur == 'mul(,' and temp is not None and c == ')':
        cur = None
        fac2 = int(temp)
        temp = None
        if enabled:
            ans += fac1 * fac2
            print(fac1, '*', fac2)
        else:
            print('disabled!')
    else:
        cur = None
        temp = None

print(ans)

