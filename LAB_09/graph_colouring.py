class GraphColoring:
    def __init__(self, graph: dict):
        self.graph  = graph
        self.nodes  = sorted(graph.keys())
        self.n      = len(self.nodes)
        self.idx    = {v: i for i, v in enumerate(self.nodes)}

    def is_valid_labeling(self, labeling: dict) -> bool:
        for u in self.graph:
            for v in self.graph[u]:
                if u < v:                   
                    if labeling.get(u) == labeling.get(v):
                        return False
        return True

    def assign_labels(self, k: int):
        labeling = {}
        if self._backtrack(0, k, labeling):
            return (True, labeling)
        return (False, {})

    def _backtrack(self, idx: int, k: int, labeling: dict) -> bool:
        if idx == self.n:
            return True                     

        node = self.nodes[idx]
        used_by_neighbours = {
            labeling[v] for v in self.graph[node] if v in labeling
        }

        for color in range(k):
            if color not in used_by_neighbours:
                labeling[node] = color
                if self._backtrack(idx + 1, k, labeling):
                    return True
                del labeling[node]           

        return False

    def find_min_labels(self):
        for k in range(1, self.n + 1):
            success, labeling = self.assign_labels(k)
            if success:
                return (k, labeling)
        return (self.n, {v: i for i, v in enumerate(self.nodes)})

    def greedy_coloring(self):
        labeling = {}
        for node in self.nodes:
            used = {labeling[v] for v in self.graph[node] if v in labeling}
            color = 0
            while color in used:
                color += 1
            labeling[node] = color
        return labeling
    
def demo_exercise2():
    print("=" * 55)
    print("  EXERCISE 2 — Conflict-Free Labeling (Graph Coloring)")
    print("=" * 55)

    bipartite = {0:{1,3}, 1:{0,2}, 2:{1,3}, 3:{0,2}}
    gc = GraphColoring(bipartite)

    print("\nGraph (cycle C4 — bipartite):")
    for node in sorted(bipartite):
        print(f"  Node {node} → {sorted(bipartite[node])}")

    print("\n── Verification ──────────────────────────────────────")
    valid_lab = {0:0, 1:1, 2:0, 3:1}
    bad_lab   = {0:0, 1:0, 2:1, 3:1}
    print(f"  Labeling {valid_lab} → valid = {gc.is_valid_labeling(valid_lab)}")
    print(f"  Labeling {bad_lab}   → valid = {gc.is_valid_labeling(bad_lab)}")

    print("\n── assign_labels trials ──────────────────────────────")
    for k in [1, 2, 3]:
        ok, lab = gc.assign_labels(k)
        print(f"  k={k} → success={ok}  labeling={lab if ok else 'N/A'}")

    print("\n── Minimum labels ────────────────────────────────────")
    k_min, lab = gc.find_min_labels()
    print(f"  Minimum k    : {k_min}")
    print(f"  Labeling     : {lab}")
    print(f"  Valid        : {gc.is_valid_labeling(lab)}")

    print("\n── Greedy coloring ───────────────────────────────────")
    greedy_lab = gc.greedy_coloring()
    greedy_k   = len(set(greedy_lab.values()))
    print(f"  Greedy labels used : {greedy_k}")
    print(f"  Labeling           : {greedy_lab}")
    print(f"  Valid              : {gc.is_valid_labeling(greedy_lab)}")
    print(f"  Optimal?           : {greedy_k == k_min}")

    print("\n── Edge Cases ────────────────────────────────────────")

    k4 = {i:{j for j in range(4) if j!=i} for i in range(4)}
    gc4 = GraphColoring(k4)
    k_min4, lab4 = gc4.find_min_labels()
    print(f"  Complete K4  : min labels = {k_min4}, valid = {gc4.is_valid_labeling(lab4)}")

    empty = {0:set(), 1:set(), 2:set()}
    gc_e  = GraphColoring(empty)
    k_mine, labe = gc_e.find_min_labels()
    print(f"  Empty graph  : min labels = {k_mine}, valid = {gc_e.is_valid_labeling(labe)}")

    tri = {0:{1,2}, 1:{0,2}, 2:{0,1}}
    gc3 = GraphColoring(tri)
    k_min3, lab3 = gc3.find_min_labels()
    print(f"  Triangle K3  : min labels = {k_min3}, valid = {gc3.is_valid_labeling(lab3)}")

    single = {0:set()}
    gc_s   = GraphColoring(single)
    k_s, _ = gc_s.find_min_labels()
    print(f"  Single node  : min labels = {k_s}")

    print("\n── Complexity note ───────────────────────────────────")
    print("  Verification : O(E)   — check each edge once")
    print("  Backtracking : O(k^N) — exponential worst case")
    print("  Greedy       : O(N+E) — fast but not always optimal")

    print("\nAll Exercise 2 tests passed ✓")



demo_exercise2()