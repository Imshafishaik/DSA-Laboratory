from collections import deque

class SocialGraphDFS:
    def __init__(self, n):
        self.n = n
        self.adj_list = {i: [] for i in range(n)}

    def add_friendship(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)


class SocialGraphBFS(SocialGraphDFS):

    def bfs(self, start_user):
        visited = {start_user}
        queue = deque([start_user])
        result = []

        while queue:
            u = queue.popleft()
            result.append(u)

            for v in self.adj_list.get(u, []):   # ✅ safer
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return result

    def bfs_with_distances(self, start_user):
        distances = {start_user: 0}
        queue = deque([start_user])

        while queue:
            u = queue.popleft()

            for v in self.adj_list.get(u, []):   # ✅ safer
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)

        return distances

    def shortest_path(self, start_user, target_user):
        if start_user == target_user:
            return [start_user]

        parent = {start_user: None}
        queue = deque([start_user])

        while queue:
            u = queue.popleft()

            for v in self.adj_list.get(u, []):
                if v not in parent:
                    parent[v] = u

                    if v == target_user:
                        return self._reconstruct_path(parent, target_user)

                    queue.append(v)

        return []

    def _reconstruct_path(self, parent, target):
        path = []
        node = target

        while node is not None:
            path.append(node)
            node = parent[node]

        return path[::-1]

    def degrees_of_separation(self, start_user, target_user):
        return self.bfs_with_distances(start_user).get(target_user, -1)

    def friends_within_k_hops(self, start_user, k):
        distances = self.bfs_with_distances(start_user)
        return {v for v, d in distances.items() if 0 < d <= k}

    def recommend_friends(self, start_user, max_recommendations=5):
        direct = set(self.adj_list.get(start_user, []))   # ✅ use set
        candidates = {}

        for friend in direct:
            for fof in self.adj_list.get(friend, []):
                if fof != start_user and fof not in direct:
                    candidates[fof] = candidates.get(fof, 0) + 1

        # ✅ stable sorting (by mutual friends desc, then user id)
        ranked = sorted(candidates.items(), key=lambda x: (-x[1], x[0]))

        return [user for user, _ in ranked[:max_recommendations]]

    def compute_average_degrees_of_separation(self):
        total, count = 0, 0

        for u in range(self.n):
            distances = self.bfs_with_distances(u)

            for v, d in distances.items():
                if v != u:
                    total += d
                    count += 1

        return total / count if count > 0 else 0.0

    def get_distance_distribution(self, start_user):
        dist = {}

        for v, d in self.bfs_with_distances(start_user).items():
            if v != start_user:
                dist[d] = dist.get(d, 0) + 1

        return dist


def test_exercise3():
    g = SocialGraphBFS(6)
    g.add_friendship(0, 1)
    g.add_friendship(1, 2)
    g.add_friendship(2, 3)
    g.add_friendship(3, 4)
    # node 5 isolated

    order = g.bfs(0)
    assert order[0] == 0
    assert set(order) == {0, 1, 2, 3, 4}

    dist = g.bfs_with_distances(0)
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[4] == 4
    assert 5 not in dist

    assert g.shortest_path(0, 4) == [0, 1, 2, 3, 4]
    assert g.shortest_path(0, 5) == []
    assert g.shortest_path(2, 2) == [2]

    assert g.degrees_of_separation(0, 4) == 4
    assert g.degrees_of_separation(0, 5) == -1
    assert g.degrees_of_separation(1, 3) == 2

    assert g.friends_within_k_hops(0, 2) == {1, 2}

    g2 = SocialGraphBFS(5)
    g2.add_friendship(0, 1)
    g2.add_friendship(0, 2)
    g2.add_friendship(1, 3)
    g2.add_friendship(2, 3)
    g2.add_friendship(1, 4)

    recs = g2.recommend_friends(0)
    assert recs[0] == 3   # 3 has 2 mutual friends with 0

    dd = g.get_distance_distribution(0)
    assert dd[1] == 1
    assert dd[4] == 1

    g3 = SocialGraphBFS(3)
    g3.add_friendship(0, 1)
    g3.add_friendship(1, 2)

    avg = g3.compute_average_degrees_of_separation()
    assert abs(avg - (8/6)) < 0.01

    g4 = SocialGraphBFS(2)
    assert g4.degrees_of_separation(0, 1) == -1

    print("Exercise 3: ALL TESTS PASSED")


test_exercise3()