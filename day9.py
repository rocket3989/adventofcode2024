from aocd import get_data
from rich import print as print

data = get_data(day=9, year=2024)


test_data ='''2333133121414131402'''


def solve1(data: str) -> int:
    ans = 0

    vals = []
    file = True
    num = 0
    for val in data.strip():
        if file:
            vals.extend([num] * int(val))
            num += 1
        else:
            vals.extend([-1] * int(val))

        file = not file

    r_pointer = len(vals) - 1
    
    for i, val in enumerate(vals):

        if val == -1:
            while vals[r_pointer] == -1:
                r_pointer -= 1

            if i >= r_pointer:
                break

            ans += i * vals[r_pointer]
            vals[i] = vals[r_pointer]
            vals[r_pointer] = -1
            r_pointer -= 1
        else:
            ans += i * val

    return ans


def solve2(data: str) -> int:
    ans = 0

    vals = []
    file = True
    num = 0

    nums = []
    spaces = []

    for val in data.strip():
        if file:
            nums.append((len(vals), int(val)))
            vals.extend([num] * int(val))
            num += 1
        else:
            spaces.append((len(vals), int(val)))
            vals.extend([-1] * int(val))

        file = not file

    for pos, length in reversed(nums):
        best_slot = (1_000_000_000, -1, -1)

        for i, (start, size) in enumerate(spaces):
            if size < length:
                continue

            if start < best_slot[0]:
                best_slot = (start, size, i)
        
        if best_slot[0] == 1_000_000_000 or best_slot[0] > pos:
            continue


        for i in range(length):
            vals[best_slot[0] + i] = vals[pos + i]
            vals[pos + i] = -1
        
        if best_slot[1] > length:
            spaces[best_slot[2]] = (best_slot[0] + length, best_slot[1] - length)
        else:
            spaces[best_slot[2]] = (1_000_000_000, 0)

    for i, val in enumerate(vals):
        if val != -1:
            ans += i * val
            

    return ans


print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))