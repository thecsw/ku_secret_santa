#!/bin/env python

import random

users = []
with open("users.txt", "r") as r:
    users = [x.replace('\n', '') for x in r.readlines()]

print(users)
temp = users

targets = []

for user in users:
    name = random.choice(users)
    while name == user or name in targets:
        name = random.choice(users)
    targets.append(name)

targets = [x + '\n' for x in targets]

with open("targets.txt", "w") as w:
    w.writelines(targets)
