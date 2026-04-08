from collections import defaultdict

class SocialGraph:
    def __init__(self, n):
        self.n = n
        self.adj_list = defaultdict(list)

    def add_friendship(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def get_degree(self, u):
        return len(self.adj_list[u])


class SocialGraphDFS(SocialGraph):

    def dfs_recursive(self, start_user: int) -> list:
        visited = set()
        result = []

        def helper(u):
            visited.add(u)
            result.append(u)
            for v in self.adj_list[u]:
                if v not in visited:
                    helper(v)

        helper(start_user)
        return result

    def dfs_iterative(self, start_user: int) -> list:
        visited = set()
        result = []
        stack = [start_user]

        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                result.append(u)
                for v in self.adj_list[u]:
                    if v not in visited:
                        stack.append(v)

        return result

    def _dfs_component(self, start: int, visited: set) -> list:
        component = []
        stack = [start]

        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                component.append(u)
                for v in self.adj_list[u]:
                    if v not in visited:
                        stack.append(v)

        return component

    def find_connected_components(self) -> list:
        visited = set()
        components = []

        for u in range(self.n):
            if u not in visited:
                component = self._dfs_component(u, visited)
                components.append(component)

        return components

    def is_connected(self) -> bool:
        return len(self.find_connected_components()) == 1

    def has_path(self, start_user: int, target_user: int) -> bool:
        if start_user == target_user:
            return True

        visited = set()
        stack = [start_user]

        while stack:
            u = stack.pop()

            if u == target_user:
                return True

            if u not in visited:
                visited.add(u)
                for v in self.adj_list[u]:
                    if v not in visited:
                        stack.append(v)

        return False

    def find_path(self, start_user: int, target_user: int) -> list:
        if start_user == target_user:
            return [start_user]

        visited = set()
        stack = [(start_user, [start_user])]

        while stack:
            u, path = stack.pop()

            if u == target_user:
                return path

            if u not in visited:
                visited.add(u)

                for v in self.adj_list[u]:
                    if v not in visited:
                        stack.append((v, path + [v]))

        return []

    def get_connected_components_sizes(self) -> list:
        return [len(c) for c in self.find_connected_components()]

    def find_largest_component(self) -> list:
        components = self.find_connected_components()
        return max(components, key=len) if components else []

    def find_isolated_users(self) -> list:
        return [u for u in range(self.n) if self.get_degree(u) == 0]

def test_exercise2():

    g = SocialGraphDFS(7)

    g.add_friendship(0, 1)
    g.add_friendship(1, 2)
    g.add_friendship(0, 2)

    g.add_friendship(3, 4)

    rec = g.dfs_recursive(0)
    itr = g.dfs_iterative(0)

    assert set(rec) == {0, 1, 2}
    assert set(itr) == {0, 1, 2}
    assert rec[0] == 0
    assert itr[0] == 0

    comps = g.find_connected_components()
    sizes = sorted([len(c) for c in comps])
    assert sizes == [1, 1, 2, 3]

    assert g.is_connected() == False

    g2 = SocialGraphDFS(3)
    g2.add_friendship(0, 1)
    g2.add_friendship(1, 2)
    assert g2.is_connected() == True

    assert g.has_path(0, 2) == True
    assert g.has_path(0, 3) == False
    assert g.has_path(5, 5) == True

    path = g.find_path(0, 2)
    assert path[0] == 0 and path[-1] == 2
    assert len(path) >= 2

    empty = g.find_path(0, 3)
    assert empty == []

    isolated = g.find_isolated_users()
    assert set(isolated) == {5, 6}

    largest = g.find_largest_component()
    assert set(largest) == {0, 1, 2}

    g3 = SocialGraphDFS(1)
    assert g3.is_connected() == True
    assert g3.find_isolated_users() == [0]
    assert g3.dfs_iterative(0) == [0]

    print("All Exercise 2 tests passed!")

test_exercise2()