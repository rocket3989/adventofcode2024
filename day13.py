from aocd import get_data
from parse import findall
from rich import print as print

from heapq import heappop, heappush

from z3 import Int, Optimize, sat

data = get_data(day=13, year=2024)


test_data ='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''


def solve1(data: str) -> int:
    ans = 0

    for section in data.split("\n\n"):
        A = [(tuple(r)) for r in findall("A: X+{:d}, Y+{:d}", section)]
        B = [(tuple(r)) for r in findall("B: X+{:d}, Y+{:d}", section)]
        
        P = [(tuple(r)) for r in findall("X={:d}, Y={:d}", section)]

        Ax, Ay = A[0]
        Bx, By = B[0]
        Px, Py = P[0]


        h = [(0, 0, 0)]
        seen = set()
        while h:
            dist, x, y = heappop(h)

            if (x, y) in seen:
                continue

            seen.add((x, y))


            if (x, y) == (Px, Py):
                ans += dist
                break

            if x > Px or y > Py:
                continue

            heappush(h, (dist + 3, x + Ax, y + Ay))
            heappush(h, (dist + 1, x + Bx, y + By))

    return ans


def solve2(data: str) -> int:
    ans = 0

    for section in data.split("\n\n"):
        A = [(tuple(r)) for r in findall("A: X+{:d}, Y+{:d}", section)]
        B = [(tuple(r)) for r in findall("B: X+{:d}, Y+{:d}", section)]
        
        P = [(tuple(r)) for r in findall("X={:d}, Y={:d}", section)]

        Ax, Ay = A[0]
        Bx, By = B[0]
        Px, Py = P[0]
        Px += 10000000000000
        Py += 10000000000000


        a_presses = Int('a_presses')
        b_presses = Int('b_presses')

        o = Optimize()
        o.add(a_presses >= 0)
        o.add(b_presses >= 0)
        o.add(a_presses * Ax + b_presses * Bx == Px)
        o.add(a_presses * Ay + b_presses * By == Py)

        o.minimize(3 * a_presses + b_presses)
        if o.check() == sat:

            ans += o.model()[a_presses].as_long() * 3 + o.model()[b_presses].as_long()

    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))