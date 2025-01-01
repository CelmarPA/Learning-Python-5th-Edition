def make_actions():
    acts = []
    for i in range(5):      # Tries to remember each i
        acts.append(lambda x: i ** x)       # But all remember same last i!
    return acts

acts = make_actions()
print(acts[0])

print(acts[0](2))       # All are 4 ** 2, 4=value of last i
print(acts[1](2))       # This should be 1 ** 2 (1)
print(acts[2](2))       # This should be 1 ** 2 (1)
print(acts[4](2))       # Only this should be 4 ** 2 (16)

def make_actions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = make_actions()

print(acts[0](2))       # 0 ** 2
print(acts[1](2))       # 1 ** 2
print(acts[2](2))       # 2 ** 2
print(acts[4](2))       # 4 ** 2
