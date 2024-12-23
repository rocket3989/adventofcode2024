from aocd import get_data
from rich import print as print
from itertools import combinations
import networkx as nx


data = get_data(day=23, year=2024)


test_data ='''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''


def solve1(data: str) -> int:
    ans = set()
    G = nx.Graph()
    for line in data.split('\n'):
        G.add_edge(*line.split('-'))

    for clique in nx.find_cliques(G):
        if len(clique) < 3:
            continue

        t_nodes = [node for node in clique if node[0] == 't']
        other_nodes = [node for node in clique if node[0] != 't']


        for comb in combinations(t_nodes, 3):
            ans.add(tuple(sorted(comb)))

        for comb in combinations(t_nodes, 2):
            for other in other_nodes:
                ans.add(tuple(sorted((*comb, other))))

        for comb in combinations(other_nodes, 2):
            for t in t_nodes:
                ans.add(tuple(sorted((*comb, t))))


    return len(ans)


def solve2(data: str) -> int:
    G = nx.Graph()
    for line in data.split('\n'):
        a, b = line.split('-')
        G.add_edge(a, b)

    clique = max(nx.find_cliques(G), key=len)
    

    return ','.join(sorted(clique))

print(solve1(test_data))
print(solve1(data))
print(solve2(test_data))
print(solve2(data))