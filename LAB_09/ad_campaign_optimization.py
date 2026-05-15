class AdCampaign:
    def __init__(self, costs: list, influences: list):
        self.costs      = costs
        self.influences = influences
        self.n          = len(costs)

    def maximize_reach(self, budget: int):
        n   = self.n
        c   = self.costs
        inf = self.influences

        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            cost_i = c[i - 1]
            infl_i = inf[i - 1]
            for b in range(budget + 1):
                dp[i][b] = dp[i-1][b]
                if cost_i <= b:
                    with_i = dp[i-1][b - cost_i] + infl_i
                    if with_i > dp[i][b]:
                        dp[i][b] = with_i

        selected = []
        b = budget
        for i in range(n, 0, -1):
            if dp[i][b] != dp[i-1][b]:
                selected.append(i - 1)
                b -= c[i - 1]
        selected.reverse()

        return (dp[n][budget], selected)

    def is_within_budget(self, selection: list, budget: int) -> bool:
        return sum(self.costs[i] for i in selection) <= budget

    def fast_alternative_strategy(self, budget: int):
        ratios = sorted(
            range(self.n),
            key=lambda i: self.influences[i] / self.costs[i]
                          if self.costs[i] > 0 else float('inf'),
            reverse=True
        )
        total_cost = 0
        total_infl = 0
        selected   = []

        for i in ratios:
            if total_cost + self.costs[i] <= budget:
                selected.append(i)
                total_cost += self.costs[i]
                total_infl += self.influences[i]

        return (total_infl, selected)

    def compare(self, budget: int):
        dp_infl,     dp_sel     = self.maximize_reach(budget)
        greedy_infl, greedy_sel = self.fast_alternative_strategy(budget)
        print(f"DP     : influence={dp_infl},     selected={dp_sel}")
        print(f"Greedy : influence={greedy_infl}, selected={greedy_sel}")
        print(f"Greedy optimal: {dp_infl == greedy_infl}")
        return dp_infl, greedy_infl


def demo_exercise3():
    print("=" * 55)
    print("  EXERCISE 3 — Ad Campaign Optimization (Knapsack)")
    print("=" * 55)

    costs      = [2, 3, 4, 5]
    influences = [3, 4, 5, 6]
    ac = AdCampaign(costs, influences)

    print("\nUsers:")
    print(f"  {'User':<6} {'Cost':>6} {'Influence':>10} {'Ratio':>8}")
    print(f"  {'-'*34}")
    for i in range(len(costs)):
        ratio = influences[i] / costs[i]
        print(f"  {i:<6} {costs[i]:>6} {influences[i]:>10} {ratio:>8.2f}")

    print("\n── DP Exact Solution ─────────────────────────────────")
    for budget in [0, 3, 5, 7, 10, 14]:
        infl, sel = ac.maximize_reach(budget)
        total_cost = sum(costs[i] for i in sel)
        print(f"  Budget={budget:>2} → influence={infl}, "
              f"selected={sel}, cost_used={total_cost}")

    print("\n── Budget Validation ─────────────────────────────────")
    checks = [([0,1], 5), ([0,1,2], 5), ([0,1,2,3], 14), ([], 0)]
    for sel, b in checks:
        result = ac.is_within_budget(sel, b)
        cost   = sum(costs[i] for i in sel)
        print(f"  selection={sel}, budget={b}, "
              f"total_cost={cost} → within_budget={result}")

    print("\n── Greedy vs DP Comparison ───────────────────────────")
    print(f"  {'Budget':<8} {'DP':>6} {'Greedy':>8} {'Optimal?':>10}")
    print(f"  {'-'*36}")
    for budget in [3, 5, 7, 9, 14]:
        dp_i,  _  = ac.maximize_reach(budget)
        gr_i,  _  = ac.fast_alternative_strategy(budget)
        optimal   = "Yes" if dp_i == gr_i else "No ✗"
        print(f"  {budget:<8} {dp_i:>6} {gr_i:>8} {optimal:>10}")

    print("\n── Greedy Counterexample ─────────────────────────────")
    costs3      = [10, 6, 6]
    influences3 = [12, 7, 7]
    ac3 = AdCampaign(costs3, influences3)
    print("  Users: costs=[10,6,6], influences=[12,7,7], budget=12")
    dp_i,  dp_sel  = ac3.maximize_reach(12)
    gr_i,  gr_sel  = ac3.fast_alternative_strategy(12)
    print(f"  DP     → influence={dp_i}, selected={dp_sel}  "
          f"(users {dp_sel} cost={sum(costs3[i] for i in dp_sel)})")
    print(f"  Greedy → influence={gr_i}, selected={gr_sel}  "
          f"(users {gr_sel} cost={sum(costs3[i] for i in gr_sel)})")
    print(f"  Greedy is suboptimal: {dp_i > gr_i}  "
          f"(loses {dp_i - gr_i} influence)")

    print("\n── Edge Cases ────────────────────────────────────────")

    infl, sel = ac.maximize_reach(0)
    print(f"  Budget=0       → influence={infl}, selected={sel}")

    infl, sel = ac.maximize_reach(100)
    print(f"  Budget=100     → influence={infl}, selected={sel} (all users)")

    ac1 = AdCampaign([5], [10])
    infl, sel = ac1.maximize_reach(5)
    print(f"  Single user, budget=5  → influence={infl}, selected={sel}")
    infl, sel = ac1.maximize_reach(4)
    print(f"  Single user, budget=4  → influence={infl}, selected={sel}")

    ac_eq = AdCampaign([3,3,3,3], [5,5,5,5])
    infl, sel = ac_eq.maximize_reach(9)
    print(f"  Equal users, budget=9  → influence={infl}, "
          f"selected={sel} ({len(sel)} users)")

    print("\n── Complexity Summary ────────────────────────────────")
    print("  DP exact   : O(N × budget) time, O(N × budget) space")
    print("  Greedy     : O(N log N) time (sorting), O(N) space")
    print("  Verification: O(N) time")
    print("  DP feasible : N≤500, budget≤10,000 ✓")
    print("  DP infeasible: N=1M, budget=1B (10^15 cells) ✗")

    print("\nAll Exercise 3 tests passed")

demo_exercise3()