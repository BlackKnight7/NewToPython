import random
import operator
import ipdb

for i in range(0, 10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}

    op = random.choice(list(ops.keys()))
    result = input("%s %s %s = " % (a, op, b))
    result = int(result)

    answer = ops.get(op)(a, b)
    if answer == result:
        print("Success")
    else:
        ipdb.set_trace()
        print("Failed")
