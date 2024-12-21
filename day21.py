from aocd import get_data
from parse import parse, findall, search
from rich import print as print
from collections import defaultdict, deque, Counter
from functools import lru_cache
from heapq import heappop, heappush
from itertools import permutations, product
import re
from tqdm import tqdm
import resource
import sys
# from z3 import Int, Optimize, sat, Solver

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

data = get_data(day=21, year=2024)


test_data ='''029A
980A
179A
456A
379A'''

directional_pad = ''' ^A
<v>'''

numeric_pad = '''789
456
123
 0A'''


directional = defaultdict(str)
for i, line in enumerate(directional_pad.split("\n")):
    for j, char in enumerate(line):
        directional[(i, j)] = char
        if char == ' ':
            directional[(i, j)] = ''

numeric_lookup = defaultdict(str)

numeric = defaultdict(str)
for i, line in enumerate(numeric_pad.split("\n")):
    for j, char in enumerate(line):
        numeric[(i, j)] = char
        numeric_lookup[char] = (i, j)
        if char == ' ':
            numeric[(i, j)] = ''

commands = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

command_lookup = {
    'A': (0, 2),
    '^': (0, 1),
    'v': (1, 1),
    '<': (1, 0),    
    '>': (1, 2)
}




def solve1(data: str) -> int:
    ans = 0

    for code in data.split("\n"):
        # print(code)

        robot1 = (0, 2)
        robot2 = (0, 2)
        robot3 = (3, 2)

        q = deque([(0, robot3, robot2, robot1, code)])

        seen = set()
        while q:
            dist, robot3, robot2, robot1, curr = q.popleft()

            if (robot1, robot2, robot3, curr) in seen:
                continue

            seen.add((robot1, robot2, robot3, curr))

            if curr == '':
                ans += dist * int(code[:3])
                print(dist, int(code[:3]))
                break

            for command, (dx, dy) in commands.items():
                new_robot1 = (robot1[0] + dx, robot1[1] + dy)

                if directional[new_robot1] == '':
                    continue

                q.append((dist + 1, robot3, robot2, new_robot1, curr))

            # human hits A
            
            if directional[robot1] in commands:
                command = commands[directional[robot1]]

                new_robot2 = (robot2[0] + command[0], robot2[1] + command[1])

                if directional[new_robot2] != '':
                    q.append((dist + 1, robot3, new_robot2, robot1, curr))
                continue

            #robot 1 hits A

            if directional[robot2] in commands:
                command = commands[directional[robot2]]

                new_robot3 = (robot3[0] + command[0], robot3[1] + command[1])

                if numeric[new_robot3] != '':
                    q.append((dist + 1, new_robot3, robot2, robot1, curr))
                continue

            #robot 2 hits A

            if numeric[robot3] != curr[0]:
                continue

            q.append((dist + 1, robot3, robot2, robot1, curr[1:]))











    return ans

robot_count = 2



def solveOther(data: str) -> int:
    ans = 0

    for code in data.split("\n"):
        # print(code)

        directional_robots = [(0, 2)] * robot_count


        numeric_robot = (3, 2)

        q = deque([(0, code, numeric_robot, *directional_robots)])

        seen = set()
        while q:
            dist, curr, numeric_robot, *directional_robots = q.popleft()

            if (curr, numeric_robot, *directional_robots) in seen:
                continue

            seen.add((curr, numeric_robot, *directional_robots))

            if curr == '':
                ans += dist * int(code[:3])
                print(code, dist)

                break

            for command, (dx, dy) in commands.items():
                temp_robot = (directional_robots[0][0] + dx, directional_robots[0][1] + dy)


                if directional[temp_robot] == '':
                    continue

                q.append((dist + 1, curr, numeric_robot, temp_robot, *directional_robots[1:]))

            # human hits A


            for i, robot in enumerate(directional_robots):
                if directional[robot] in commands:
                    command = commands[directional[robot]]

                    # print(command)

                    # print(directional_robots[:10], numeric_robot)

                    if i == len(directional_robots) - 1:
                        
                        numeric_robot = (numeric_robot[0] + command[0], numeric_robot[1] + command[1])

                        if numeric[numeric_robot] != '':
                            q.append((dist + 1, curr, numeric_robot, *directional_robots))
                        break

                    directional_robots[i + 1] = (directional_robots[i + 1][0] + command[0], directional_robots[i + 1][1] + command[1])

                    if directional[directional_robots[i + 1]] != '':
                        q.append((dist + 1, curr, numeric_robot, *directional_robots))
                    break

            else:
                if numeric[numeric_robot] == curr[0]:
                    q.append((dist + 1, curr[1:], numeric_robot, *directional_robots))


    return ans


def solve2hv(data: str) -> int:
    ans = 0

    @lru_cache
    def cost(start, end, robot):

        if robot == 1:
            return abs(end[0] - start[0]) + abs(end[1] - start[1])

        if start[0] == end[0]:
            vertical = ''
        if start[0] > end[0]:
            vertical = '^'
        if start[0] < end[0]:
            vertical = 'v'

        if start[1] == end[1]:
            horizontal = ''
        if start[1] > end[1]:
            horizontal = '<'
        if start[1] < end[1]:
            horizontal = '>'

        if not vertical and not horizontal:
            return 1
        
        if not vertical:
            ret = 1 + abs(end[1] - start[1])
            ret += cost(command_lookup['A'], command_lookup[horizontal], robot - 1)
            ret += cost(command_lookup[horizontal], command_lookup['A'], robot - 1)
            return ret
        
        if not horizontal:
            ret = 1 + abs(end[0] - start[0])
            ret += cost(command_lookup['A'], command_lookup[vertical], robot - 1)
            ret += cost(command_lookup[vertical], command_lookup['A'], robot - 1)
            return ret
        
        horizontal_vertical = 1 + abs(end[0] - start[0]) + abs(end[1] - start[1])

        horizontal_vertical += cost(command_lookup['A'], command_lookup[horizontal], robot - 1)
        horizontal_vertical += cost(command_lookup[horizontal], command_lookup[vertical], robot - 1)
        horizontal_vertical += cost(command_lookup[vertical], command_lookup['A'], robot - 1)

        vertical_horizontal = 1 + abs(end[0] - start[0]) + abs(end[1] - start[1])

        vertical_horizontal += cost(command_lookup['A'], command_lookup[vertical], robot - 1)
        vertical_horizontal += cost(command_lookup[vertical], command_lookup[horizontal], robot - 1)
        vertical_horizontal += cost(command_lookup[horizontal], command_lookup['A'], robot - 1)

        return min(horizontal_vertical, vertical_horizontal)


    ans = 0

    for code in data.split("\n"):

        code = 'A' + code
        dist = 0


        for a, b in zip(code, code[1:]):
            start = numeric_lookup[a]
            end = numeric_lookup[b]

            if start[0] == end[0]:
                vertical = ''
            if start[0] > end[0]:
                vertical = '^'
            if start[0] < end[0]:
                vertical = 'v'

            if start[1] == end[1]:
                horizontal = ''
            if start[1] > end[1]:
                horizontal = '<'
            if start[1] < end[1]:
                horizontal = '>'

            if not vertical and not horizontal:
                dist += 1
                continue

            if not vertical:
                dist += 1 + abs(end[1] - start[1])
                dist += cost(command_lookup['A'], command_lookup[horizontal], robot_count)
                dist += cost(command_lookup[horizontal], command_lookup['A'], robot_count)
                continue

            if not horizontal:
                dist += 1 + abs(end[0] - start[0])
                dist += cost(command_lookup['A'], command_lookup[vertical], robot_count)
                dist += cost(command_lookup[vertical], command_lookup['A'], robot_count)
                continue

            horizontal_vertical = 1 + abs(end[0] - start[0]) + abs(end[1] - start[1])
            horizontal_vertical += cost(command_lookup['A'], command_lookup[horizontal], robot_count)
            horizontal_vertical += cost(command_lookup[horizontal], command_lookup[vertical], robot_count)
            horizontal_vertical += cost(command_lookup[vertical], command_lookup['A'], robot_count)

            vertical_horizontal = 1 + abs(end[0] - start[0]) + abs(end[1] - start[1])
            vertical_horizontal += cost(command_lookup['A'], command_lookup[vertical], robot_count)
            vertical_horizontal += cost(command_lookup[vertical], command_lookup[horizontal], robot_count)
            vertical_horizontal += cost(command_lookup[horizontal], command_lookup['A'], robot_count)


            dist += min(horizontal_vertical, vertical_horizontal)

        ans += dist * int(code[1:4])
        print(code, dist)

    return ans



def solve2(data: str) -> int:
    ans = 0

    @lru_cache
    def cost(start, end, robot):

        if robot == 0:
            return abs(end[0] - start[0]) + abs(end[1] - start[1])
        

        h = [(0, start, command_lookup['A'])]
        seen = set()

        while h:
            dist, location, cursor = heappop(h)

            if (location, cursor) in seen:
                continue

            seen.add((location, cursor))

            if location == end:
                return dist + cost(cursor, command_lookup['A'], robot - 1)

            for command, (dx, dy) in commands.items():
                new_location = (location[0] + dx, location[1] + dy)

                if directional[new_location] == '':
                    continue
                
                heappush(h, (dist + cost(cursor, command_lookup[command], robot - 1) + 1, new_location, command_lookup[command]))



    ans = 0

    for code in data.split("\n"):

        code = 'A' + code
        code_cost = 0


        for a, b in zip(code, code[1:]):
            start = numeric_lookup[a]
            end = numeric_lookup[b]

            q = deque([(start, command_lookup['A'], 0)])

            h = [(0, start, command_lookup['A'])]
            seen = set()

            while h:
                dist, location, cursor = heappop(h)

                if (location, cursor) in seen:
                    continue

                seen.add((location, cursor))

                if location == end:
                    code_cost += dist + cost(cursor, command_lookup['A'], robot_count)

                for command, (dx, dy) in commands.items():
                    new_location = (location[0] + dx, location[1] + dy)

                    if numeric[new_location] == '':
                        continue

                    heappush(h, (dist + cost(cursor, command_lookup[command], robot_count) + 1, new_location, command_lookup[command]))


        ans += dist * int(code[1:4])
        print(code, dist)

    return ans

# print(solve1(test_data))
# print(solve1(data))
print(solveOther(test_data))
print(solve2(test_data))
print(solveOther(data))
print(solve2(data))
