import json
from aocd import get_data
from parse import findall
from rich import print as print

data = get_data(day=14, year=2024)

test_data ='''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''


def solve1(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("p={:d},{:d} v={:d},{:d}", data)]

    robots = []
    for row in parsed:
        robots.append(row)

    n, m = 101, 103

    q1, q2, q3, q4 = 0, 0, 0, 0

    for robot in robots:
        final_x = ((robot[0] + 100 * robot[2]) + 10000 * n) % n
        final_y = ((robot[1] + 100 * robot[3]) + 10000 * m) % m


        if final_x < n // 2:
            if final_y < m // 2:
                q1 += 1
            elif final_y > m // 2:
                q2 += 1
        elif final_x > n // 2:
            if final_y < m // 2:
                q3 += 1
            elif final_y > m // 2:
                q4 += 1
    
    return q1 * q2 * q3 * q4


def solve2(data: str) -> int:
    parsed = [(tuple(r)) for r in findall("p={:d},{:d} v={:d},{:d}", data)]

    
    json.dump(parsed, open('day14robots.json', 'w'))
    return "saved robot data"

print(solve1(test_data))
print(solve1(data))
print(solve2(data)) 