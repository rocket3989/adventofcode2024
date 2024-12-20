import math
from aocd import get_data
from parse import findall
from rich import print as print
import functools

data = get_data(day=17, year=2024)


test_data ='''Register A: 705
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''

def solve1(data: str) -> int:
    registers = [(tuple(r)) for r in findall(": {:d}", data)]

    print(registers)
    A = registers[0][0]
    B = registers[1][0]
    C = registers[2][0]

    program = [int(x) for x in data.split('Program: ')[1].split(',')]

    PC = 0 

    while PC < len(program):
        op = program[PC]
        operand = program[PC + 1]

        combo = operand
        match operand:
            case 4:
                combo = A
            case 5:
                combo = B
            case 6:
                combo = C
            case 7:
                pass


        match op:
            case 0:
                A = math.trunc(A / (2 ** combo))

            case 1:
                B ^= operand

            case 2:
                B = combo % 8

            case 3:
                if A == 0:
                    PC += 2
                    continue
                PC = operand
                continue

            case 4:
                B ^= C

            case 5:
                print(combo % 8, end=',')

            case 6:
                B = math.trunc(A / (2 ** combo))

            case 7:
                C = math.trunc(A / (2 ** combo))

        PC += 2

    print()
    ans = 0

    return ans


def solve2(data: str) -> int:
    program = [int(x) for x in data.split('Program: ')[1].split(',')]

    @functools.cache
    def search(a, depth):
        print(a, depth)
        if depth == -1:
            return a

        for a_option in range(8):

            b_option = a_option

            a_curr = a << 3 | a_option
            b_option ^= 1
            c = math.trunc(a_curr / (2 ** b_option))

            b_option ^= c
            b_option ^= 4

            if b_option % 8 == program[depth]:
                x = search(a << 3 | a_option, depth - 1)
                if x:
                    return x

        return None

    return search(0, len(program) - 1)

print(solve1(test_data))
print(solve1(data))
# print(solve2(test_data))
print(solve2(data))