from aocd import get_data
from parse import findall
from rich import print
import re

data = get_data(day=3, year=2024)


test_data ='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

def solve1(data):
    parsed = [(tuple(r)) for r in findall("mul({:d},{:d})", data)]
    ans = 0
    for a, b in parsed:
        ans += a * b

    print(ans)


def solve2(data: str):
    ans = 0
    events = []

    muls = re.finditer(r"mul\(([0-9]+),([0-9]+)\)", data)
    for mul in muls:
        events.append((mul.start(), 'mul', mul.group(1), mul.group(2)))
    
    dos = re.finditer(r"do\(\)", data)
    for do in dos:
        events.append((do.start(), 'do'))

    donts = re.finditer(r"don't\(\)", data)
    for dont in donts:
        events.append((dont.start(), 'dont'))

    events.sort()

    do = True

    for event in events:
        if event[1] == 'do':
            do = True
        elif event[1] == 'dont':
            do = False
        elif do:
            ans += int(event[2]) * int(event[3])

    print(ans)
                
solve1(data)
solve2(data)

