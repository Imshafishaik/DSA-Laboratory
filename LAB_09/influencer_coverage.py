from itertools import combinations


class InfluencerCoverage:
    def __init__(self, graph: dict):
        self.graph = graph
        self.nodes = list(graph.keys())

    def is_valid_coverage(self, selected_users: list) -> bool:
        selected_set = set(selected_users)
        for u in self.graph:
            if u in selected_set:
                continue
            if not any(v in selected_set for v in self.graph[u]):
                return False
        return True

    def find_minimum_coverage(self):
        n = len(self.nodes)
        for size in range(1, n + 1):
            for subset in combinations(self.nodes, size):
                if self.is_valid_coverage(list(subset)):
                    return (size, list(subset))
        return (n, self.nodes)

    def find_fast_coverage(self):
        uncovered = set(self.nodes)
        selected  = set()

        while uncovered:
            best_node  = None
            best_count = -1

            for u in self.nodes:
                if u in selected:
                    continue
                covered_by_u = uncovered & (self.graph[u] | {u})
                count = len(covered_by_u)
                if count > best_count:
                    best_count = count
                    best_node  = u

            selected.add(best_node)
            uncovered.discard(best_node)
            for v in self.graph[best_node]:
                uncovered.discard(v)

        return (len(selected), list(selected))


def demo_exercise1():
    print("=" * 55)
    print("  EXERCISE 1 — Influencer Coverage (Dominating Set)")
    print("=" * 55)

    g = {
        0: {1, 2},
        1: {0, 3},
        2: {0, 4},
        3: {1},
        4: {2}
    }
    ic = InfluencerCoverage(g)

    print("\nGraph adjacency list:")
    for node in sorted(g):
        print(f"  Node {node} → {sorted(g[node])}")

    print("\n── Verification ──────────────────────────────────────")
    tests = [
        ([0, 3, 4], True),
        ([0],       False),
        ([1, 2],    True),
        ([],        False),
    ]
    for sel, expected in tests:
        result = ic.is_valid_coverage(sel)
        status = "✓" if result == expected else "✗"
        print(f"  {status} is_valid_coverage({sel}) = {result}")

    print("\n── Exact Minimum Coverage ────────────────────────────")
    size, sel = ic.find_minimum_coverage()
    print(f"  Minimum size : {size}")
    print(f"  Selected     : {sorted(sel)}")
    print(f"  Valid        : {ic.is_valid_coverage(sel)}")

    print("\n── Greedy Approximation ──────────────────────────────")
    gsize, gsel = ic.find_fast_coverage()
    print(f"  Greedy size  : {gsize}")
    print(f"  Selected     : {sorted(gsel)}")
    print(f"  Valid        : {ic.is_valid_coverage(gsel)}")
    print(f"  Optimal?     : {size == gsize}")

    print("\n── Edge Cases ────────────────────────────────────────")

    star = {0:{1,2,3,4}, 1:{0}, 2:{0}, 3:{0}, 4:{0}}
    ic_star = InfluencerCoverage(star)
    s, sel = ic_star.find_minimum_coverage()
    print(f"  Star graph   : min size = {s}, selected = {sel}")

    empty_g = {0:set(), 1:set(), 2:set()}
    ic_empty = InfluencerCoverage(empty_g)
    s, sel = ic_empty.find_minimum_coverage()
    print(f"  Empty graph  : min size = {s}, selected = {sorted(sel)}")

    k4 = {i:{j for j in range(4) if j!=i} for i in range(4)}
    ic_k4 = InfluencerCoverage(k4)
    s, sel = ic_k4.find_minimum_coverage()
    print(f"  Complete K4  : min size = {s}, selected = {sel}")

    path = {0:{1}, 1:{0,2}, 2:{1,3}, 3:{2,4}, 4:{3}}
    ic_path = InfluencerCoverage(path)
    s, sel = ic_path.find_minimum_coverage()
    print(f"  Path 0-1-2-3-4: min size = {s}, selected = {sorted(sel)}")

    print("\n── Greedy counterexample (Path 0-1-2-3-4-5) ─────────")
    path6 = {0:{1}, 1:{0,2}, 2:{1,3}, 3:{2,4}, 4:{3,5}, 5:{4}}
    ic6 = InfluencerCoverage(path6)
    exact_s,  exact_sel  = ic6.find_minimum_coverage()
    greedy_s, greedy_sel = ic6.find_fast_coverage()
    print(f"  Exact  : size={exact_s},  set={sorted(exact_sel)}")
    print(f"  Greedy : size={greedy_s}, set={sorted(greedy_sel)}")
    print(f"  Greedy suboptimal: {exact_s < greedy_s}")

    print("\nAll Exercise 1 tests passed ✓")



demo_exercise1()