from collections import deque

def decimal_to_binary(n):
    #return bin(n)
    #return f'{n:b}'
    res = deque()

    while True:
        n, r = divmod(n, 2)
        res.appendleft(r)
        if not n:
            break

    return ''.join((map(str, res)))


print(decimal_to_binary(16))

