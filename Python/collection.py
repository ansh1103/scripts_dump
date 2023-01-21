import collections

# A double-ended queue, or deque, supports adding and removing elements from either end. The more commonly used stacks
# and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.
d = collections.deque()
d.extend('abcd')

d.extendleft('h')
print(list(d))

d.extend('i')
print(d)

# rotating deque
d.rotate(2)
print(d)

d.rotate(-2)
print(d)

# consuming from deque
while True:
    print(d.pop())
