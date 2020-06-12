import random
from collections import defaultdict, Counter

with open("input.txt") as f:
    words = f.read()
    model = defaultdict(Counter)

_length = 10

for i in range(len(words) - _length):
    state = words[i:i + _length]
    _next = words[i + _length]
    model[state][_next] += 1

state = random.choice(list(model))
out = list(state)
for i in range(400):
    out.extend(random.choices(list(model[state]), model[state].values()))
    state = state[1:] + out[-1]
print(''.join(out))

# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here

