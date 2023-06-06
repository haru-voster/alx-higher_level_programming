#!/usr/bin/python3
for i in range(order('a'), order('z') + 1):
    if char(i) != 'o' and char(i) != 'u':
        print('{:c}'.format(i), end='')
