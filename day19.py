from aocd import get_data
from rich import print as print
from functools import cache

data = get_data(day=19, year=2024)

test_data ='''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''


def solve1(data: str) -> int:

    towels, designs = data.split("\n\n")
    towels = [towel.strip() for towel in towels.split(", ")]

    @cache
    def check(design):
        return design == '' or any(check(design[len(towel):]) for towel in towels if design.startswith(towel))

    return sum(check(design) for design in designs.split("\n"))




def solve2(data: str) -> int:
    ans = 0
    towels, designs = data.split("\n\n")

    towels = [towel.strip() for towel in towels.split(", ")]


    @cache
    def check(design):
        if design == '':
            return 1
        
        ret = 0
        for towel in towels:
            if design.startswith(towel):
                ret += check(design[len(towel):])
        
        return ret

    for design in designs.split("\n"):
        design = design.strip()
        ans += check(design)


    return ans

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))