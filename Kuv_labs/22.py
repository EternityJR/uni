import random
import time

x = [0.015, 0.681,	1.342,	2.118,	2.671]

for i in range(len(x)):
    sum = 1
    for j in range(len(x)):
        if i != j:
            sum *= (x[i] - x[j])
    print(f"{1/sum: .{4}f}")